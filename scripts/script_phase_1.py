# Import des packages et modules nécessaires à l'extraction de données
import requests
from bs4 import BeautifulSoup

# Import de csv pour le transfert des données sur un fichier
import csv

root = "https://books.toscrape.com/"
data_category = [
    "product_url", "universal_product_code", "title", "price_including_tax",
    "price_excluding_tax", "number_available", "product_description",
    "category", "review_rating", "image_url"
]

def scrape_book(book_url):
    # Récupération du code source de la page via une requête HTTP
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Test pour vérifier qu'on a bien obtenu le code
    # print(soup) ––––> OK

    # Après inspection sur le site de chaque élément à extraire,
    # on peut les isoler dans des variables en utilisant leurs
    # balises, id et/ou class via BeautifulSoup :
    product_url = book_url
    upc = soup.find('th', string="UPC").find_next('td').text
    title = soup.find('h1').text
    price_incl_tax_raw = soup.find('th', string="Price (incl. tax)").find_next('td').text
    price_incl_tax = str(price_incl_tax_raw.lstrip('Â£') + " £")
    price_excl_tax_raw = soup.find('th', string="Price (excl. tax)").find_next('td').text
    price_excl_tax = str(price_excl_tax_raw.lstrip('Â£') + " £")
    number_available = soup.find('th', string="Availability").find_next('td').text
    product_description = soup.find('div', id="product_description").find_next('p').text
    category = soup.find('ul', class_='breadcrumb').find_all('a')[-1].text

    # Le paragraphe contenant le review_rating affiche dans sa balise:
    # <p class='star-rating Four'> Il faut distinguer 2 classes ici indexées
    # 0 pour 'star-rating' et 1 pour 'Four'
    rating_tag = soup.find('p', class_='star-rating')
    rating_class = rating_tag['class'][1]
    # Dictionnaire pour convertir le texte en valeur numérique
    ratings_map = {
        "One": "1/5",
        "Two": "2/5",
        "Three": "3/5",
        "Four": "4/5",
        "Five": "5/5"
    }
    # Conversion de la note en utilisant le dictionnaire
    review_rating = ratings_map.get(rating_class, "Note non trouvée")

    image_url = soup.find('img')['src']
    image_url = 'https://books.toscrape.com/' + image_url.lstrip('../..')

    # En vue de l'écriture des données extraites dans un fichier .csv
    # organisé, on commence par distinguer, dans 2 listes, les noms
    # des catégories de donnée et les variables qui contiennent leurs valeurs :

    data_values = [
        product_url, upc, title, price_incl_tax, price_excl_tax, number_available,
        product_description, category, review_rating, image_url
    ]

    print(data_values)

    # Écriture du fichier .csv dans le répertoire data de notre projet
    # en utilisant csv importé en début de script.
    # On ouvre ce nouveau fichier avec le mode writer et en spécifiant
    # à Python d'ignorer les caractères de fin de ligne et d'éviter l'ajout
    # de lignes vides intermédiaires.
    return data_values

if __name__ == '__main__':
    url = f'{ root }catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html' #noqa
    data_values = scrape_book(url)
    with open('../data/product_datas.csv', mode='w', newline='', encoding="utf-8") as file :
        writer = csv.writer(file, delimiter=',') # On spécifie la ',' pour séparer les données.
        writer.writerow(data_category) # La ligne d'en-tête, contenant les catégories
        writer.writerow(data_values) # La ligne de données
