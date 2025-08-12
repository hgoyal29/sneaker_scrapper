from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import os
import pandas as pd
import re


query = input("Search: ").strip().lower()
page_count = int(input("How many pages you want to scrape?: "))

folder_path = f"data/{query}"    #creates a folder for each query
os.makedirs(folder_path, exist_ok=True)

file = 0
for i in range(1, page_count + 1):
    driver = webdriver.Chrome()

    driver.get(f"https://www.ebay.com/sch/i.html?_sop=12&_nkw={query}&_stpos=32608&_fcid=1&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={i}")
    time.sleep(2)  

    elems = driver.find_elements(By.CLASS_NAME, "su-card-container")
    print(f"{len(elems)} items found")
    print(f"You have searched for '{query}' on page {i} of eBay")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        soup = BeautifulSoup(d, 'html.parser')

        
        ti = soup.find("div", attrs={"class": 's-card__title'})
        title = ti.get_text().lower() if ti else "no-title"

        match = re.search(r'(?:size|sz|us)\s*[:\-]?\s*(\d+\.?\d*)', title.lower())
        size = match.group(1) if match else "unknown"


        # Save HTML to specific folder
        with open(f"{folder_path}/{query}_size{size}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

    driver.quit()


data = {'title': [], 'sold_price': [], 'link': [], 'sold_date': [], 'size': [], 'condition' : []}

for file in os.listdir(folder_path):
    with open(f"{folder_path}/{file}", 'r', encoding='utf-8') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    ti = soup.find("div", attrs={"class": 's-card__title'})
    title = ti.get_text().strip().lower() if ti else "no-title"

    t = soup.find("div")
    l = t.find("a") if t else None
    link = l["href"] if l else "no-link"

    condition = "no-condition"
    c = soup.find("span", class_='su-styled-text secondary default')
    if c:
        text = c.get_text().strip().lower()
        if "new" in text:
            condition = "Brand New"
        elif "used" in text:
             condition = "Used"
        else:
           condition = text.title()

 
  

    p = soup.find("span", attrs={"class": 's-card__price'})
    sold_price = p.get_text().strip() if p else "no-price"

    date = soup.find("span", attrs={"class": 'su-styled-text'})
    sold_date = date.get_text().replace("Sold ", "").strip() if date else "no-date"

    match = re.search(r'size\s?:?\s?(\d+\.?\d*)\s?(y)?', title)
    size = match.group(1) if match else "unknown"

    data['title'].append(title)
    data['link'].append(link.strip().lower())
    data['sold_price'].append(sold_price)
    data['sold_date'].append(sold_date)
    data['size'].append(size)
    data['condition'].append(condition) 

df = pd.DataFrame(data=data)
df = df.drop_duplicates(subset=['title']).reset_index(drop=True)
df = df[df['size'] != "unknown"].reset_index(drop=True)
df['size'] = df['size'].astype(float) #converting in float for better sorting


os.makedirs("saved", exist_ok=True)   #saves the final CSV in a 'saved' folder
csv_file = f"saved/data_{query}.csv"
df.to_csv(csv_file, index=False)

print(f"\n✅ Saved {len(df)} rows to {csv_file} with size info.")