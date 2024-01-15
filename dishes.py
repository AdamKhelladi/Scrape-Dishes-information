# Scrape https://www.buonissimo.it:

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import string
import time

master_list = []

def get_ingredient_info(letter, page):

  url = f"https://www.buonissimo.it/ingredienti/lettera/{letter}/pagina/{page}/" 

  html = requests.get(url).text 
  soup = bs(html, "html.parser")

  dishes = soup.find_all("div", {"class": "lstCont"})

  for dish in dishes: 
    title = dish.find("h2").text
    description = dish.find("p").text

    dish_info = {
      "Letter" : letter,
      "Title" : title,
      "Description" : description,
    }

    master_list.append(dish_info)

  df = pd.DataFrame(master_list)
  df.to_csv("dishes_info.csv", index=False)

for letter in string.ascii_uppercase:
  for page in range(1, 20): 
    get_ingredient_info(letter, page)
    time.sleep(1)

print("file created.")