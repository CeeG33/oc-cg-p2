# Scraper du site Books to Scrape
Projet n°2 - Utilisez les bases de Python pour l'analyse de marché - Auteur : Ciran GÜRBÜZ

Date : Mars 2023

Après avoir téléchargé le contenu du repository, veuillez l'extraire dans un dossier spécifique sur votre ordinateur. Ensuite, suivez ces étapes dans l'ordre afin de faire fonctionner le code et pouvoir extraire les données du site Books to Scrape (http://books.toscrape.com/index.html) :

python==3.11.2

beautifulsoup4==4.11.2

certifi==2022.12.7

charset-normalizer==3.1.0

idna==3.4

requests==2.28.2

soupsieve==2.4


## 1 - Installation des logiciels requis

### 1.1 - Python

Il est impératif d'installer la dernière version de Python que vous pourrez retrouver sur le site officiel de Python : https://www.python.org/downloads/

### 1.2 - Création et activation de l'environnement virtuel

#### a) Ouvrir un terminal de commande et se placer dans le dossier contenant les fichiers du repository.
#### b) Créer l'environnement virtuel avec la ligne de commande suivante : 
```python -m venv "env"```
#### c) Activer l'environnement virtuel avec la ligne de commande suivante : 
```env/Scripts/activate```

### 1.3 - Installation des packages

#### a) Une fois l'environnement virtuel activé, installer les packages avec la commande suivante : 
```pip install -r requirements.txt```

### 1.4 - Visual Studio Code

Pour pouvoir lire le code Python, il est recommandé d'installer un logiciel dédié comment Visual Studio Code que vous pourrez trouver ici : https://code.visualstudio.com/

## 2 - Exécution du script

#### a) Veuillez ouvrir le fichier ```p2scrap3.py``` et vérifier que la variable main_url contient bien le lien vers le site Books to Scrape comme suit :
```python
main_url = "http://books.toscrape.com/index.html"
```

#### b) Exécutez le fichier ```p2scrap3.py``` soit en cliquant sur le bouton Run Python File dans l'interface Visual Studio Code, soit en tapant la commande suivante dans le terminal de commande :
```python p2scrap3.py```

#### c) Attendre que les données et les images se chargent.

#### d) Vous voilà maintenant avec un nouveau dossier books_img contenant les images de couverture de chaque livre triées par catégorie et classées selon le n° UPC du livre et un fichier contenant les données brutes de chaque livre par catégorie  d'ouvrage !

## 3 - Conversion des données brutes des fichiers CSV en tableau

#### a) Veuillez ouvrir n'importe quel fichier CSV avec Excel.
#### b) Allez dans l'onglet ```Données``` puis ```Obtenir des données > À partir d'un fichier > À partir d'un fichier texte/CSV```
#### c) L'origine du fichier ainsi que le délimiteur doivent automatiquement réglées sur respectivement "65001 : Unicode (UTF-8)" et "Virgule". Si ce n'est pas le cas, veuillez les régler manuellement et cliquez sur "Charger". Vous voilà maintenant avec votre premier fichier de données sous forme de tableau !

