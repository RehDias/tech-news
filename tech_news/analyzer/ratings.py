import tech_news.database as db


# Requisito 10
def top_5_news():
    top_five_news = db.get_collection().find().sort([
      ("comments_count", -1), ("title", 1)]).limit(5)
    tuple_news = [(new['title'], new['url']) for new in top_five_news]
    return tuple_news


# Requisito 11
def top_5_categories():
    news = db.find_news()
    categories = [new['category'] for new in news]
    cat_count = [
     {"cat": category, "count": categories.count(
      category)} for category in sorted(set(categories))]
    sorted_categories = sorted(
      cat_count, key=lambda cat: cat.get('count'), reverse=True)
    top_five = [category['cat'] for category in sorted_categories]
    return top_five[:5]
