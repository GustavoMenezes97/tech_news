from ..database import search_news
from datetime import datetime

# https://www.programiz.com/python-programming/datetime/strftime


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
    try:
        dd_mm_yyyy = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    content_list = search_news({"timestamp": dd_mm_yyyy})

    formated_content_list = []

    for content in content_list:
        formated_content_list.append((content["title"], content["url"]))

    return formated_content_list


# Requisito 9
def search_by_category(category):
    content_list = search_news({
        "category": {"$regex": category, "$options": "i"}
    })

    formated_content_list = []

    for content in content_list:
        formated_content_list.append((content["title"], content["url"]))

    return formated_content_list
