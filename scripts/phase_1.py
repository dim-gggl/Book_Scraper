import requests
from bs4 import BeautifulSoup
import csv

# Main URL that we will call and join to any relative URL
ROOT = "https://books.toscrape.com/"
# The headers of every CSV files we are going to create
HEADERS = [
    "product_url", "universal_product_code", "title", "price_including_tax",
    "price_excluding_tax", "number_available", "product_description",
    "category", "review_rating", "image_url"
]
# A relative output path to the repertory the program is launch from
OUTPUT_FILE_PATH = f'./data'


def scrape_book(url):
    """
    Scrape a chosen book page
    :param url: The url of the book page (str)
    :return: The expected book datas
    """
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_url = str(url)
        upc = soup.find('th', string="UPC").find_next('td').text
        title = soup.find('h1').text

        price_incl_tax_raw = soup.find('th', string="Price (incl. tax)").find_next('td').text.strip()
        price_incl_tax = f"£ {price_incl_tax_raw.lstrip('Â£')}"
        price_excl_tax_raw = soup.find('th', string="Price (excl. tax)").find_next('td').text
        price_excl_tax = f"£ {price_excl_tax_raw.lstrip('Â£')}"

        number_available = soup.find('th', string="Availability").find_next('td').text

        description_tag = soup.find('div', id="product_description")
        if description_tag:
            product_description = description_tag.find_next('p').text
        else:
            product_description = "No description"
        category = soup.find('ul', class_='breadcrumb').find_all('a')[-1].text

        rating_tag = soup.find('p', class_='star-rating')
        rating_class = rating_tag['class'][1]

        ratings_map = {
            "One": "1/5",
            "Two": "2/5",
            "Three": "3/5",
            "Four": "4/5",
            "Five": "5/5"
        }

        review_rating = ratings_map.get(rating_class, "Note non trouvée")

        image_url_src = soup.find('img')['src']
        image_url = ROOT + image_url_src.lstrip('../..')

        return [
            product_url, upc, title, price_incl_tax, price_excl_tax, number_available,
            product_description, category, review_rating, image_url
        ]
    else:
        return None

if __name__ == '__main__':
    url = f'{ROOT}catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html' #noqa
    product_data = scrape_book(url)
    if product_data:
        try:
            with open(f'{OUTPUT_FILE_PATH}script1_book_details.csv', mode='w', newline='', encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerow(HEADERS)
                writer.writerow(product_data)
                print(f"Book's data saved in : {OUTPUT_FILE_PATH}")
        except FileNotFoundError:
            print(f"Erreur : {OUTPUT_FILE_PATH} est invalide")
    else:
        print("Erreur : impossible de récupérer les données du livres")