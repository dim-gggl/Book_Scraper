import requests
from bs4 import BeautifulSoup
import csv
from typing import TextIO
from script_phase_1 import (scrape_book, root, product_data_headers, output_file_rep)


def get_next_page(soup, current_url) :
    next_page_tag = soup.find('li', class_='next')
    if next_page_tag:
        next_page_url = next_page_tag.find('a')['href']
        return '/'.join(current_url.split('/')[:-1]) + next_page_url
    return None


def scrape_category(category_url):

    current_url = category_url + "index.html"
    all_books_data = []


    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for a in soup.find_all('article', class_='product_pod'):
            book_link_tag = soup.find('a')['href']
            book_link = [ root + "catalogue/" + book_link_tag.lstrip('../') ]
            book_datas = scrape_book(book_link)
            if book_datas:
                all_books_data.append(book_datas)
            else:
                print("No data returned by scrape_book(book_link)")


        current_url = get_next_page(soup, current_url)

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