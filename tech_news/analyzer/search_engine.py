import datetime
import tech_news.database as db


# Requisito 6
def search_by_title(title):
    news = db.search_news({
      "title": {
        "$regex": title,
        "$options": 'i'
        }
    })
    tuple_news = [(new['title'], new['url']) for new in news]
    return tuple_news


# Requisito 7
def search_by_date(date):
    try:
        data = datetime.datetime.strptime(date, '%Y-%m-%d')
        news_by_date = db.search_news({
          "timestamp": datetime.date.strftime(data, "%d/%m/%Y")
        })
    except ValueError:
        raise ValueError('Data inválida')
    tuple_news = [(new['title'], new['url']) for new in news_by_date]
    return tuple_news


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
