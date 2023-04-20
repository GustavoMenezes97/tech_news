import requests
import time
from parsel import Selector

# https://pt.stackoverflow.com/questions/449990/como-obter-a-primeira-palavra-de-um-texto-em-python
# https://pt.stackoverflow.com/questions/107841/fun%C3%A7%C3%A3o-equivalente-ao-trim-fun%C3%A7%C3%A3o-para-remover-espa%C3%A7os-extras-no-in%C3%ADcio-e-fim
# https://stackoverflow.com/questions/58415452/how-to-extract-href-value-from-rel-tag-in-python


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    list_of_links = selector.css(".cs-overlay-link ::attr(href)").getall()
    return list_of_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link_next_page = selector.css(".next ::attr(href)").get()
    return link_next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical'] ::attr(href)").get()
    title = selector.css(".entry-title ::text").get().rstrip()
    timestamp = selector.css(".meta-date ::text").get()
    writer = selector.css(".url.fn.n ::text").get()
    reading_time = selector.css(".meta-reading-time ::text").get().split()[0]
    summary = "".join(
        selector.css(".entry-content > p:first-of-type ::text").getall()
    ).rstrip()
    category = selector.css(".label ::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
