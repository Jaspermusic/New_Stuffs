# Basic working from an existing HTML code [Simple.html]

# pip install beautifulsoup4
#     [beautifulsoup4 -> Latest Version, beautifulsoup -> Older Version]
# pip install lxml
#     [Parser to parse HTML]
#     [Parser fills Error lines of HTML lines]
#     [Best parser for beautifulsoup is lxml]
# pip install html5lib
#     [Another famous Parser, but not need to download now]
# pip install requests
#     [Request library, an alternative to urllib]

from bs4 import BeautifulSoup
import requests

html_file = open('Simple.html')
soup = BeautifulSoup(html_file, 'lxml')

print(soup)
#   [prints the HTML file with no indentation]
print(soup.prettify())
#   [prettify() -> prints the same indentation as the HTML code]

match = soup.title
#   [Obtains title from HTML code]
print(match)
#   [<title>Test - A Sample Website</title> -> Extra HTML tags is attached]

match = soup.title.text
print(match)
#   [Only prints the text leaving Tags behind]

match = soup.div.text
#   [Obtain the first <div> from HTML]
match = soup.find('div', class_='footer').text
#   [Obtain the <div> with class as 'footer']
#   [class_ is used because, python already has an keyword 'class']

article = soup.find('div', class_='article')
#   [Gets the content of 1st article]
#   [1st article has Headline and paragraph]
#   [Don't include .text, if added further classification can't be made]
headline = article.h2.a.text
#   [Gets headline from 1st article]
#   [Gets data from h2 -> Header2 tag and a -> anchor tag]
print(headline)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
#   [find_all gives every article in the HTML code]
