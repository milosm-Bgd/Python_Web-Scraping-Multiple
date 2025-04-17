import requests

#importing the entire moduel 
import bs4  #BeautifulSoup library 
#using BeautifulSoup we can create a "soup" object that contains all the "ingredients" of the webpage.

#import just the class that we need
#we go with this approach 
from bs4 import BeautifulSoup 

# BeautifulSoup(MARKUP, HTML PARSER)
# OPtions for PArser: 
#1. "html.parser" (Python's html parser)
#2. "lxml" (lxml's HTML parser)
#3. "lxml-xml" (lxml's XML parser)
#4 "html5lib" (html5lib)

# http://books.toscrape.com/catalogue/page-1.html
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
type(base_url)

base_url.format('1')
res = requests.get(base_url.format('1'))
soup = BeautifulSoup(res.text,"lxml")
soup

#selecting the div with class .procuct_pod 

  soup.select(".product_pod")
  #placing the result content into the variable products 
  products = soup.select(".product_pod")

  example = products[0]

  example

  list(example.children)

  #what if a given tag has more than just one class?
example.select('.star-rating.Three')


# An Example for Homework
# Scrape just the Books with 2 stars Rating
# Note two_star_titles = [] that right from the start, we know that there are 50 pages

two_star_titles = []

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1,51):

  scrape_url = base_url.format(n)
  res = requests.get(scrape_url)
  
  soup = BeautifulSoup(res.text, "lxml")
  books = soup.select('.product_pod')

  for book in books:
    if len(book.select('.star-rating.Two')) != 0:
      two_star_titles.append(book.select('a')[1]['title'])

two_star_titles
