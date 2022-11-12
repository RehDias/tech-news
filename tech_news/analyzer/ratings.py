import tech_news.database as db


# Requisito 10
def top_5_news():
    top_five_news = db.get_collection().find().sort([
      ("comments_count", -1), ("title", 1)]).limit(5)
    tuple_news = [(new['title'], new['url']) for new in top_five_news]
    return tuple_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
