# Importation des packages requis
import requests
from bs4 import BeautifulSoup
import csv
import p2scrap1 as s1

# Début Phase 2

main_url = "http://books.toscrape.com/index.html"
main_url_html = s1.req_html(main_url)
html_soup = s1.parse_html(main_url_html)

# Définition de la catégorie à scraper
category = 'Poetry'

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
url_cat_req_first = s1.req_html(url_cat)
url_cat_soup_first = s1.parse_html(url_cat_req_first)

# Extraction de l'URL de tous les livres de la page
def extract_books_url(url_cat):
    url_cat_req = s1.req_html(url_cat)
    url_cat_soup = s1.parse_html(url_cat_req)
    ol = url_cat_soup.find('ol', class_='row')
    h3 = ol.find_all('h3')
    h3_a = []
    for a in h3:
        list_a = a.find('a')
        h3_a.append(list_a)

    hrefs = []
    for a in h3_a:
        href = a.get('href')
        hrefs.append('http://books.toscrape.com/catalogue/' + href.replace('../../../', ''))
    return hrefs

hrefs_list = extract_books_url(url_cat)

# Détection de la pagination
presence_next = url_cat_soup_first.find('li', class_='next')

if presence_next:
    
    links_cat = []
    
    pagination = url_cat_soup_first.find('li', class_='current').string.strip()
    
    nb_page_cat = int(pagination[10])
    
    pages = 1
   
    for page in range(2, nb_page_cat + 1):
        pages += 1
        links_cat.append(url_cat + 'page-' + str(page) + '.html')
    
    for link in links_cat:
        hrefs_list.extend(extract_books_url(link))

"""
for link in hrefs_list:
    s1.book_data(link)


# Création liste des catégories
list_categories = []
for cat in nav_list_a:
    list_categories.append(cat.string.strip())

print(list_categories)

"""