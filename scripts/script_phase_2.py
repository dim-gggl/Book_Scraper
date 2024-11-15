import requests
from bs4 import BeautifulSoup
import csv
from script_phase_1 import scrape_book, data_category

# On commence par la création d'une fonction pour lister les liens
# de tous les livres d'une page
def get_product_links(soup):
    # On crée la liste qui contiendra liens extraits
    product_links = []
    for h3 in soup.find_all('h3'):
        raw_link = h3.a['href']
        product_link = "https://books.toscrape.com/catalogue/" + raw_link.lstrip('../../')
        product_links.append(product_link)
    return product_links

def scrape_category(category_url):
    current_url = category_url # Cette variable est celle qui va éplucher les pages,
    # on spécifie ici que son point de départ est la page d'accueil de la catégorie
    product_links = [] # Notre future liste de liens

    # current_url s'arrêtera à la page qui ne contient plus de page suivante,
    # le nombre de pages différant d'une catégorie à l'autre, on préfère une boucle
    # while
    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = get_product_links(soup) # Tant que la variable contiendra un lien,
        print(links)
        # les liens de chaque livre qui s'y trouvent seront extraits
        product_links.extend(links) # et ajoutés à cette liste
        next_page_tag = soup.find('li', class_='next') # On y cherche l'accès page suivante
        if next_page_tag:
            next_page_url = next_page_tag.find('a')['href'] # On extrait le morceau de lien
            # Et on l'ajoute minutieusement à l'URL du site :
            current_url = '/'.join(current_url.split('/')[:-1]) + '/' + next_page_url
        else:
            current_url = None # Lorsque le scraping de la dernière page est fait, la variable
            # ne contient plus de lien vers une autre page. La boucle s'arrête.

    category_name = category_url.rstrip('./').split('/')[-1]
    with open(f'../data/{category_name}_product_details.csv', mode='w', newline='', encoding="utf-8") as file:
        data_values = []
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data_category)

        for link in product_links:
            data_values += scrape_book(link)

        writer.writerows(data_values)


if __name__ == '__main__':
    category_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/'
    scrape_category(category_url)