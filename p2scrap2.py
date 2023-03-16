# Importation des packages requis
import requests
from bs4 import BeautifulSoup
import csv
import p2scrap1 as s1

# Début Phase 2

# Définition de l'url de la page principale
main_url = "http://books.toscrape.com/index.html"

# Appel de l'url de la page principale
main_url_html = s1.reqHtml(main_url)

# Parsage des données
html_soup = s1.parseHtml(main_url_html)

# Définition de la catégorie à scraper
category = 'Mystery'

# Fonction pour la rechercher l'URL de la catégorie
def url_cat_find(category):
    nav_list_ul = html_soup.find('ul', class_='nav nav-list')
    nav_list_a = nav_list_ul.find_all('a')
    find_cat = None

    for a in nav_list_a:
        if category in a.text:
            find_cat = a
            break
    base_url = 'http://books.toscrape.com/'

    url_gen = base_url + find_cat['href']
    return url_gen

url_cat = url_cat_find(category)

# Appel de l'URL de la catégorie souhaitée
url_cat_cible = s1.reqHtml(url_cat)

# Parsage des données de la catégorie souhaitée
cat_cible_soup = s1.parseHtml(url_cat_cible)

# Extraction de l'URL de tous les livres de la page
def extract_books_url(cat_cible_soup):
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
    return hrefs
liste_hrefs = extract_books_url(cat_cible_soup)

print(liste_hrefs)  

"""
presence_next = cat_cible_soup.find('li', class_='next')
if presence_next:
    url_cat_page2 = url_cat.replace('index', 'page-2')



# Création liste des catégories
list_categories = []
for cat in nav_list_a:
    list_categories.append(cat.string.strip())

print(list_categories)
"""