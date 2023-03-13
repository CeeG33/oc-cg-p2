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
#titre_livre = html_soup.find('li', class_='active').string
ul_elements = html_soup.find('ul', class_='breadcrumb')
li_elements = ul_elements.find_all('li')
cat_livre = li_elements[2]
titre_livre2 = li_elements[3]

#extrait la description du livre
description_livre = html_soup.find_all('p')[3].string

#notation du livre
note1 = html_soup.find('p', class_="star-rating One")
if note1: 
        print('1/5')

note2 = html_soup.find('p', class_="star-rating Two")
if note2: 
        print('2/5')

note3 = html_soup.find('p', class_="star-rating Three")
if note3: 
        print('3/5')

note4 = html_soup.find('p', class_="star-rating Four")
if note4: 
        print('4/5')

note5 = html_soup.find('p', class_="star-rating Five")
if note5: 
        print('5/5')

#print(product_page_url)
print()
#print(infos_livres)
print()
#print(titre_livre2.text)
print()
#print(description_livre)
#print(cat_livre.text)
