# Import des packages et modules nécessaires à l'extraction de données
import requests
from bs4 import BeautifulSoup

# Import de csv pour le transfer des données sur un fichier
import csv

# L'URL du livre choisi contenu dans une variable :
url = \
    ('https://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the'
     '-1936-berlin-olympics_992/index.html')

# Récupération du code source de la page via une requête
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Test pour vérifier qu'on a bien obtenu le code
# print(soup) ––––> OK

# Après inspection sur le site de chaque élément à extraire,
# on peut les isoler dans des variables en utilisant leurs
# balises, id et/ou class via BeautifulSoup :

product_url = url
upc = soup.find('th', text='UPC').find_next('td').text
title = soup.find('h1').text
price_incl_tax = soup.find('th', text="Price including tax").find_next('td').text
price_excl_tax = soup.find('th', text="Price excluding tax").find_next('td').text
number_available = soup.find('th', text='Availability').find_next('td').text
product_description = soup.find('div', id="product_description").find_next('p').text
category = soup.find('ul', class_='breadcrumb').find_all('a')[-1].text
review_rating = soup.find('p', class_='rating-star')['class'][1]
image_url = soup.find('img')['src']
image_url = 'https://books.toscrape.com' + image_url.lstrip('../..')

# En vue de l'écriture des données extraites dans un fichier .csv
# organisé, on commence par distinguer, dans 2 listes, les noms
# des catégories de donnée et les variables qui contiennent leurs valeurs :

data_category = [
    "product_url", "universal_product_code", "title", "price_including_tax",
    "price_excluding_tax", "number_available", "product_description",
    "category", "review_rating", "image_url"
]

data_value = [
    product_url, upc, title, price_incl_tax, price_excl_tax, number_available,
    product_description, category, review_rating, image_url
]

# Écriture du fichier .csv dans le répertoire data de notre projet
# en utilisant csv importé en début de script.
# On ouvre ce nouveau fichier avec le mode writer et en spécifiant
# à Python d'ignorer les caractères de fin de ligne et d'éviter l'ajout
# de lignes vides intermédiaires.

with open('../data/product_datas.csv', mode='w', newline='') as file :
    writer = csv.writer(file, delimiter=',') # On spécifie la ',' pour séparer les données.
    writer.writerow(data_category) # La ligne d'en-tête, contenant les catégories
    writer.writerow(data_value) # La ligne de données







