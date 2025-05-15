import requests
from bs4 import BeautifulSoup
from phase_1 import ROOT

def get_categories_urls() -> dict:
    results = {}
    response = requests.get(ROOT)
    soup = BeautifulSoup(
        response.text,
        'html.parser'
        )

    category_tags = soup.find(
        'ul',
        class_="nav nav-list"
        ).find_all('a')[1:]

    for tag in category_tags:
            relative_url = tag['href']
            category_url = ROOT + relative_url
            category_name = tag.text.strip()
            results[category_name] = category_url

    return results

