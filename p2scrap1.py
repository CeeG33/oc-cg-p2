import requests
from bs4 import BeautifulSoup
import csv
import os

product_page_url = 'http://books.toscrape.com/catalogue/the-faith-of-christopher-hitchens-the-restless-soul-of-the-worlds-most-notorious-atheist_495/index.html'

def req_html(product_page_url):
      return requests.get(product_page_url)

def parse_html(product_page_html):
      return BeautifulSoup(product_page_html.content, 'html.parser')

def book_data(product_page_url):

      product_page_html = req_html(product_page_url)
      html_soup = parse_html(product_page_html)
            
      # Extrait l'UPC, les prix et la disponibilité (extract)
      table = html_soup.find('table', class_='table table-striped')
      table_td = table.find_all('td')
      upc = table_td[0].text
      price_excl_tax = table_td[2].text
      price_incl_tax = table_td[3].text
      availability = table_td[5].text

      # Extrait le titre et la catégorie du livre (extract)
      ul_elements = html_soup.find('ul', class_='breadcrumb')
      li_elements = ul_elements.find_all('li')
      cat_book = li_elements[2].text.strip()
      title_book = li_elements[3].text.strip()

      # Extrait la description du livre (extract)
      description_book = html_soup.find_all('p')[3].string

      # Extrait la note du livre (extract)
      div_book = html_soup.find('div', class_='col-sm-6 product_main')
      p_marks = div_book.find_all('p', class_='star-rating')
      book_mark = None
      for mark in p_marks:
            if 'One' in mark['class']:
                  book_mark = '1_5'
            elif 'Two' in mark['class']:
                  book_mark = '2_5'
            elif 'Three' in mark['class']:
                  book_mark = '3_5'
            elif 'Four' in mark['class']:
                  book_mark = '4_5'
            elif 'Five' in mark['class']:
                  book_mark = '5_5'

      # Extrait l'URL de l'image de couverture (extract), la télécharge puis la stocke dans un dossier selon l'UPC du livre
      div_img = html_soup.find('div', class_='item active')
      src = div_img.find('img')['src']
      img_url = 'http://books.toscrape.com/' + src.replace('../../', '') 
      img_directory = 'books_img/' + cat_book.replace(' ', '') + '/' + upc.replace(' ', '') + '/'
      img_title = upc.replace(' ', '') + '.jpg'
      if not os.path.exists(img_directory): 
            os.makedirs(img_directory)
      response_img = requests.get(img_url)
      with open(img_directory + img_title, 'wb') as f:
            f.write(response_img.content) 
     
      data_list = [
            [product_page_url, 
            upc,
            title_book,
            price_incl_tax, 
            price_excl_tax, 
            availability,
            description_book, 
            cat_book, 
            book_mark, 
            img_url]
      ]

      headers = [
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

      csv_file_name = 'books' + cat_book.replace(' ', '') + '.csv'
      
      with open(csv_file_name, 'a', encoding="utf-8", newline='') as csv_file:
            if os.stat(csv_file_name).st_size == 0:
                  writer = csv.writer(csv_file, delimiter=',')
                  writer.writerow(headers)
                  writer.writerows(data_list)
            else:
                  writer = csv.writer(csv_file, delimiter=',')
                  writer.writerows(data_list)