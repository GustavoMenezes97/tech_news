from ..database import search_news


# Requisito 7
def search_by_title(title):
    content_list = search_news({
        "title": {"$regex": title, "$options": "i"}
    })

    formated_content_list = []

    for content in content_list:
        formated_content_list.append((content["title"], content["url"]))

    return formated_content_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
