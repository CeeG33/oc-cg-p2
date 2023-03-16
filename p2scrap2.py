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
category = 'Sequential Art'

# Fonction pour rechercher l'URL de la catégorie
def url_cat_find(category):
    nav_list_ul = html_soup.find('ul', class_='nav nav-list')
    nav_list_a = nav_list_ul.find_all('a')
    find_cat = None

    for a in nav_list_a:
        if category in a.text:
            find_cat = a
            break
    base_url = 'http://books.toscrape.com/'

    url_gen = base_url + find_cat['href'].replace('index.html', '')
    return url_gen

url_cat = url_cat_find(category)
req_url_cat = s1.reqHtml(url_cat)
soup_url_cat = s1.parseHtml(req_url_cat)

# Extraction de l'URL de tous les livres de la page
def extract_books_url(url_cat):
    url_cat_cible = s1.reqHtml(url_cat)
    cat_cible_soup = s1.parseHtml(url_cat_cible)
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

liste_hrefs = extract_books_url(url_cat)

# Détection de la pagination
presence_next = soup_url_cat.find('li', class_='next')

if presence_next:
    
    links_cat = []
    
    pagination = soup_url_cat.find('li', class_='current').string.strip()
    
    nb_page_cat = int(pagination[10])
    
    pages = 1
   
    for page in range(2, nb_page_cat + 1):
        pages += 1
        links_cat.append(url_cat + 'page-' + str(page) + '.html')
    
    for link in links_cat:
        liste_hrefs.extend(extract_books_url(link))

s1.donnees_livre('http://books.toscrape.com/catalogue/tsubasa-world-chronicle-2-tsubasa-world-chronicle-2_949/index.html')

"""
# Création liste des catégories
list_categories = []
for cat in nav_list_a:
    list_categories.append(cat.string.strip())

print(list_categories)

if presence_next:
    url_next = presence_next.find('a')
    url_next_href = url_cat + url_next['href']
    liste_hrefs.extend(extract_books_url(url_next_href))
"""