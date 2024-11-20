import requests
from bs4 import BeautifulSoup
import csv
from script_phase_1 import (scrape_book, root,
                            product_data_headers, output_file_rep, product_data)


def get_product_links(soup):
    product_links = []
    for h3 in soup.find_all('h3'):
        raw_link = h3.a['href']
        product_link = f"{root}catalogue/{raw_link.lstrip('../../')}"
        product_links.append(product_link)
    print(product_links)
    return product_links



def scrape_category(category_url):

    current_url = category_url
    product_links = []
    # le nombre de pages différant d'une catégorie à l'autre, on préfère une boucle
    # while
    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = get_product_links(soup)
        if links:
            print(f"{len(links)} de liens trouvés sur {current_url}")
            product_links.extend(links)
            print(product_links)

        next_page_tag = soup.find('li', class_='next') # On y cherche l'accès page suivante
        if next_page_tag:
            next_page_url = next_page_tag.find('a')['href']
            current_url = '/'.join(current_url.split('/')[:-1]) + '/' + next_page_url
        else:
            current_url = None
            print("No tag found for next page url")

    if not product_links:
        print("No product links found")
        return

    # On prépare le fichiers CSV
    category_name = category_url.rstrip('./').split('/')[-1]
    output_file = f'{output_file_rep}{category_name}_product_details.csv'


    with open(output_file, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data_category)

    for link in product_links:
        product_data += scrape_book(link)
        writer.writerows(product_data)


if __name__ == '__main__':
    category_url = f"'{root}catalogue/category/books/mystery_3/"
    scrape_category(category_url)