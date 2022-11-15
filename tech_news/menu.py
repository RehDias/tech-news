from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
  search_by_title,
  search_by_tag,
  search_by_category,
  search_by_date)
from tech_news.analyzer.ratings import top_5_categories, top_5_news
import sys


# Requisito 12
def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por tag;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.", end=''.strip())
    try:
        while True:
            opcao_sel = input("\nopção: ")
            func_names = [zero, one, two, three, four, five, six, seven]
            menu_items = dict(enumerate(func_names, start=0))
            selected = menu_items[int(opcao_sel)]
            selected()
    except (KeyError, ValueError):
        print("Opção inválida", file=sys.stderr)
    except Exception:
        sys.stderr.read()


def zero():
    number_news = input("Digite quantas notícias serão buscadas: ")
    print(get_tech_news(int(number_news)))


def one():
    titulo = input("Digite o título: ")
    print(search_by_title(titulo))


def two():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(date))


def three():
    tag = input("Digite a tag: ")
    print(search_by_tag(tag))


def four():
    category = input("Digite a categoria: ")
    print(search_by_category(category))


def five():
    print(top_5_news())


def six():
    print(top_5_categories())


def seven():
    print("Encerrando script")
    sys.exit()
    SystemExit
