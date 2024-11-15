import requests
from bs4 import BeautifulSoup
import csv

# On commence par la création d'une fonction pour lister les liens
# de tous les livres d'une page
def get_product_links_one_page(url):
    try: # On appréhende des erreurs de requête HTTP
        response = requests.get(url)
        if response.status_code == 200:
           soup = BeautifulSoup(response.text, 'html.parser')
           # On crée la liste qui contiendra liens extraits
           product_links = []
           for a in soup.select('h3 > a'):
               raw_link = a['href']
               product_link = "https://books.toscrape.com/catalogue/" + raw_link.lstrip('../../')
               product_links.append(product_link)
           return product_links
        else: # On affiche une erreur pour éviter le plantage du code
             print("Erreur : Impossible de récupérer la page catégorie")
    finally:
        return []

# On prépare les variables pour une boucle while permettant d'appeler
# notre fonction et de l'appliquer à chaque page de la catégorie
category_url_main = 'https://books.toscrape.com/catalogue/category/books/mystery_3/'
current_url = category_url_main # Cette variable est celle qui va éplucher les pages,
# on spécifie ici que son point de départ est la page d'accueil de la catégorie
product_links = [] # Notre future liste de liens

# current_url s'arrêtera à la page qui ne contient plus de page suivante,
# le nombre de pages différant d'une catégorie à l'autre, on préfère une boucle
# while
while current_url:
    links = get_product_links_one_page(current_url) # Tant que la variable contiendra un lien,
    # les liens de chaque livre qui s'y trouvent seront extraits
    product_links.extend(links) # et ajoutés à cette liste
    response = requests.get(current_url) # On effectue une nouvelle requête par page
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        next_page_tag = soup.find('li', class_='next') # On y cherche l'accès page suivante
        if next_page_tag:
            next_page_url = next_page_tag.find('a')['href'] # On extrait le morceau de lien
            # Et on l'ajoute minutieusement à l'URL du site :
            current_url = '/'.join(current_url.split('/')[:-1]) + '/' + next_page_url
        else:
            current_url = None # Lorsque le scraping de la dernière page est fait, la variable
            # ne contient plus de lien vers une autre page. La boucle s'arrête.
    else: # Ici aussi prise en compte d'éventuelles erreurs de requête :
        print(f"Erreur : Impossible de récupérer la page suivante à {current_url}")
    break

data_category = [
    "product_url", "universal_product_code", "title", "price_including_tax",
    "price_excluding_tax", "number_available", "product_description",
    "category", "review_rating", "image_url"
    ]
data_values = []

# On ajoute une variable contenant la catégorie pour le nom du fichier CSV :
category_name = category_url_main.rstrip('./').split('/')[-1]

with open(f'../data/{category_name}_product_details.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data_category)

    for link in product_links:
        response = requests.get(link)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            product_url = link
            upc = soup.find('th', string="UPC").find_next('td').text
            title = soup.find('h1').text
            price_incl_tax_raw = soup.find('th', string="Price (incl. tax)").find_next('td').text
            price_incl_tax = price_incl_tax_raw.replace("Â", "").strip()
            price_excl_tax_raw = soup.find('th', string="Price (excl. tax)").find_next('td').text
            price_excl_tax = price_excl_tax_raw.replace("Â", "").strip()
            number_available = soup.find('th', string="Availability").find_next('td').text
            product_description_title = soup.find('div', id="product_description")
            if product_description_title:
               product_description = product_description_title.find_next('p').text
            else:
                print("Description non disponible")
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
            image_url = soup.find('img')['src']
            image_url = 'https://books.toscrape.com/' + image_url.lstrip('../..')

            # Ajouter les données dans la liste data_values
            data_values.append(
                [product_url, upc, title, price_incl_tax, price_excl_tax, number_available, product_description, category,
                 review_rating, image_url])
        else:
            print(f"Erreur : Impossible de récupérer la page produit pour {link}")

    # Écrire toutes les données dans le CSV
    category_name = category_url_main.rstrip('./').split('/')[-1]
    writer.writerows(data_values)
