# Importation des packages requis
import requests
from bs4 import BeautifulSoup
import csv

# Début Phase 1

# Définition de l'URL
product_page_url = "http://books.toscrape.com/catalogue/the-black-maria_991/index.html"

# Fonction pour faire appel à une URL
def reqHtml(product_page_url):
      html = requests.get(product_page_url)
      return html

product_page_html = reqHtml(product_page_url)

# Fonction pour parser le code HTML
def parseHtml(product_page_html):
      soup = BeautifulSoup(product_page_html.content, 'html.parser')
      return soup

html_soup = parseHtml(product_page_html)
      
# Extrait l'UPC, les prix et la disponibilité
tableau = html_soup.find('table', class_='table table-striped')
tableau_td = tableau.find_all('td')
upc = tableau_td[0].text
priceExclTax = tableau_td[2].text
priceInclTax = tableau_td[3].text
availability = tableau_td[5].text

# Extrait le titre du livre (extract)
#titre_livre = html_soup.find('li', class_='active').string (variante)
ul_elements = html_soup.find('ul', class_='breadcrumb')
li_elements = ul_elements.find_all('li')
cat_livre = li_elements[2].text.strip()
titre_livre2 = li_elements[3].text.strip()

# Extrait la description du livre (extract)
description_livre = html_soup.find_all('p')[3].string

# Extrait la note du livre (extract)
div_livre = html_soup.find('div', class_='col-sm-6 product_main')
p_notes = div_livre.find_all('p', class_='star-rating')
note_livre = None
for note in p_notes:
      if 'One' in note['class']:
            note_livre = '1_5'
      elif 'Two' in note['class']:
            note_livre = '2_5'
      elif 'Three' in note['class']:
            note_livre = '3_5'
      elif 'Four' in note['class']:
            note_livre = '4_5'
      elif 'Five' in note['class']:
            note_livre = '5_5'

# Extrait l'URL de l'image de couverture (extract)
div_img = html_soup.find('div', class_='item active')
src = div_img.find('img')['src']
img_url = 'http://books.toscrape.com/' + src.replace('../../', '') 

# Liste de la data à charger
liste_data = [
      [product_page_url, 
      upc,
      titre_livre2,
      priceInclTax, 
      priceExclTax, 
      availability,
      description_livre, 
      cat_livre, 
      note_livre, 
      img_url]
]

# Définition des en-têtes
en_tete = [
      'product_page_url', 
      'universal_ product_code_(upc)', 
      'title', 
      'price_including_tax', 
      'price_excluding_tax', 
      'number_available', 
      'product_description', 
      'category', 
      'review_rating', 
      'image_url'
]

# Création du fichier CSV
with open('blackMariaData.csv', 'w') as fichier_csv:
      writer = csv.writer(fichier_csv, delimiter=',')
      writer.writerow(en_tete)
      writer.writerows(liste_data)

# Fin Phase 1
