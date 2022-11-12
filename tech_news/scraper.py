import requests
import time
import re
import unicodedata
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, headers={
          "user-agent": "Fake user-agent"}, timeout=3)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = []
    for new in selector.css('div.archive-main'):
        news = new.css("""article.entry-preview div.post-outer
        div div div.cs-overlay a::attr(href)""").getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_link = selector.css('div.nav-links a.next::attr(href)').get()
    return next_link


# Requisito 4
def scrape_noticia(html_content):
    seletor = Selector(html_content)
    text = seletor.css('div.entry-content p/*').get()
    REGEX = re.compile(r'<[^>]+>')
    # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
    about = {
      "url": seletor.css('link[rel~="canonical"]::attr(href)').get(),
      "title": unicodedata.normalize('NFKC', seletor.css('h1::text').get())
      .strip(),
      "timestamp": seletor.css('.meta-date::text').get(),
      "writer": seletor.css('li.meta-author span.author *::text').get(),
      "comments_count": len(seletor.css('ol.comment-list').getall()),
      "summary": unicodedata.normalize('NFKC', REGEX.sub('', text)).strip(),
      # https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python
      "tags": seletor.css('section.post-tags ul li a::text').getall(),
      "category": seletor.css('div.meta-category span.label::text').get(),
    }
    return about


# Requisito 5
def get_tech_news(amount):
    base_url = 'https://blog.betrybe.com/'
    html_content = fetch(base_url)
    links = scrape_novidades(html_content)
    news_list = []
    count = 0
    for index in range(amount):
        if count == len(links):
            count = 0
            next_page = scrape_next_page_link(html_content)
            html_content = fetch(next_page)
            links = scrape_novidades(html_content)
        news_page = fetch(links[count])
        news_content = scrape_noticia(news_page)
        news_list.extend([news_content])
        count += 1
    create_news(news_list)
    return news_list
