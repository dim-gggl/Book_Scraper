import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from script_phase_1 import (scrape_book, root, product_data_headers, output_file_rep)


def scrape_category(category_url):

    current_url = f'{category_url}index.html'
    all_books_data = []

    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        book_link_tags = soup.find_all('article', class_='product_pod')
        for tag in book_link_tags:
            book_link_tag = tag.find('a')
            if book_link_tag and 'href' in book_link_tag.attrs:
                relative_url = book_link_tag['href']
                absolute_url = urljoin(current_url, relative_url)

                book_data = scrape_book(absolute_url)
                if book_data:
                    all_books_data.append(book_data)
                else:
                    print(f"Impossible de scraper les données pour {absolute_url}")

        next_page_tag = soup.find('li', class_='next')
        if next_page_tag:
            next_page_url = next_page_tag.find('a')['href']
            current_url = urljoin(current_url, next_page_url)
        else:
            current_url = None

    return all_books_data


if __name__ == '__main__':

    category_url = f"{root}catalogue/category/books/historical-fiction_4/"
    category_name = category_url.rstrip('./').split('/')[-1]
    output_file = f"{output_file_rep}/{category_name}_product_details.csv"

    category_books_data = scrape_category(category_url)

    if category_books_data:
        with open(output_file, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(product_data_headers)
            writer.writerows(category_books_data)
        print(f"Données de la catégorie '{category_name}' sauvegardées")
    else:
        print(f"Aucune donnée trouvée pour la catégorie '{category_name}'")
