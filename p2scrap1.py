# importation des packages requis
import requests
from bs4 import BeautifulSoup

#définition de l'url
product_page_url = "http://books.toscrape.com/catalogue/the-black-maria_991/index.html"

#appel de l'url
product_page_html = requests.get(product_page_url)

#parsage des données
html_soup = BeautifulSoup(product_page_html.content, 'html.parser')

#trouve toutes les cellules du tableau contenant les principales informations concernant le livre (extract)
infos = html_soup.find_all('td')

#transforme les données récoltées en liste (transform)
infos_livres = []
for info in infos:
    infos_livres.append(info.string)

#extrait le titre du livre
titre_livre = html_soup.find('li', class_='active').string

#extrait la description du livre
description_livre = html_soup.find_all('p')[3].string

print(product_page_url)
print()
print(infos_livres)
print()
print(titre_livre)
print()
print(description_livre)