import requests
from bs4 import BeautifulSoup
import csv
import p2scrap1 as s1
import p2scrap2 as s2

# Début Phase 3
main_url = "http://books.toscrape.com/index.html"
main_url_html = s1.req_html(main_url)
html_soup = s1.parse_html(main_url_html)

nav_list_ul = html_soup.find('ul', class_='nav nav-list')
nav_list_a = nav_list_ul.find_all('a')

# Création liste des catégories > déduction liste URLs de toutes les catégories
category = []
for cat in nav_list_a[1:]:
    category.append(cat.string.strip())

urls_categories = []
for cats in category:
    urls_categories.append(s2.url_cat_find(cats))

all_books_url = []

for url in urls_categories:
    all_books_url.extend(s2.books_n_pages(url))
   
for link in all_books_url:
    s1.book_data(link)



