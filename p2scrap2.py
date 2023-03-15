# Importation des packages requis
import requests
from bs4 import BeautifulSoup
import csv

# Début Phase 2

# Définition de l'url de la page principale
main_url = "http://books.toscrape.com/index.html"

# Appel de l'url de la page principale
main_url_html = requests.get(main_url)

# Parsage des données
html_soup = BeautifulSoup(main_url_html.content, 'html.parser')

# Définition de la catégorie à scraper
category = 'Sequential Art'

# Recherche de l'URL de la catégorie
nav_list_ul = html_soup.find('ul', class_='nav nav-list')
nav_list_a = nav_list_ul.find_all('a')
find_cat = None

for a in nav_list_a:
    if category in a.text:
        find_cat = a
        break
base_url = 'http://books.toscrape.com/'

url_cat = base_url + find_cat['href']

# Appel de l'URL de la catégorie souhaitée
url_cat_cible = requests.get(url_cat)

# Parsage des données de la catégorie souhaitée
cat_cible_soup = BeautifulSoup(url_cat_cible.content, 'html.parser')

ol = cat_cible_soup.find('ol', class_='row')
h3 = ol.find_all('h3')
h3_a = []
for lesA in h3:
    liste_a = lesA.find('a')
    h3_a.append(liste_a)

hrefs = []
for a in h3_a:
    href = a.get('href')
    hrefs.append('http://books.toscrape.com/catalogue/' + href.replace('../../../', ''))

presence_next = cat_cible_soup.find('li', class_='next')
if presence_next:
    url_cat_page2 = url_cat.replace('index', 'page-2')
print(url_cat_page2)

"""
list_categories = []
for cat in nav_list_a:
    list_categories.append(cat.string.strip())

print(list_categories)
"""