# Importation des packages requis
import requests
from bs4 import BeautifulSoup

# Définition de l'url
product_page_url = "http://books.toscrape.com/catalogue/the-black-maria_991/index.html"

# Appel de l'url
product_page_html = requests.get(product_page_url)

# Parsage des données
html_soup = BeautifulSoup(product_page_html.content, 'html.parser')

# Trouve toutes les cellules du tableau contenant les principales informations concernant le livre (extract)
infos = html_soup.find_all('td')

# Extrait
tableau = html_soup.find('table', class_='table table-striped')
tableau_td = tableau.find_all('td')
upc = tableau_td[0].text
priceExclTax = tableau_td[2].text
priceInclTax = tableau_td[3].text
availability = tableau_td[5].text

# Extrait le titre du livre (extract)
#titre_livre = html_soup.find('li', class_='active').string
ul_elements = html_soup.find('ul', class_='breadcrumb')
li_elements = ul_elements.find_all('li')
cat_livre = li_elements[2]
titre_livre2 = li_elements[3]

# Extrait la description du livre (extract)
description_livre = html_soup.find_all('p')[3].string

# Extrait la note du livre (extract)
div_livre = html_soup.find('div', class_='col-sm-6 product_main')
notation1 = div_livre.find('p', class_='star-rating One')
notation2 = div_livre.find('p', class_='star-rating Two')
notation3 = div_livre.find('p', class_='star-rating Three')
notation4 = div_livre.find('p', class_='star-rating Four')
notation5 = div_livre.find('p', class_='star-rating Five')

if notation1:
      note_livre = '1/5'
elif notation2:
      note_livre = '2/5'
elif notation3:
      note_livre = '3/5'
elif notation4:
      note_livre = '4/5'
elif notation5:
      note_livre = '5/5'

# Extrait l'URL de l'image de couverture (extract)
div_img = html_soup.find('div', class_='item active')
src = div_img.find('img')['src']
img_url = 'http://books.toscrape.com/' + src.replace('../../', '') 


print(product_page_url)
print()
print(upc)
print()
print(titre_livre2.text)
print()
print(priceInclTax)
print()
print(priceExclTax)
print()
print(availability)
print()
print(description_livre)
print()
print(cat_livre.text)
print()
print(note_livre)
print()
print(img_url)