from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text

# print(html_text)
#<Response [200]> means ok

# print(dir(html_text))
#   prints the obects on the page

souped_html = BeautifulSoup(html_text, 'lxml')
# With lxml, you can easily create, parse, and query XML and HTML documents
 
countries = souped_html.find_all('h3')
# print(countries)
 
# for country in countries:
#     print(country.text.strip())
 
# df = pd.DataFrame(country.text.strip() for country in countries)
# print(df)

country_capitals = souped_html.find_all('span', class_= "country-capital")

# for capital in country_capitals:
#     print(capital.text.strip())

df = pd.DataFrame({
    "Country": [country. text. strip() for country in countries],
    "Capital": [capital.text.strip() for capital in country_capitals]
    })

print(df)