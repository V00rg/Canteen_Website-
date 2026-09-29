import requests
from bs4 import BeautifulSoup 
import pandas as pd 

url = "http://10.24.11.32:5001/menu"

response = requests.get(url)

soup=BeautifulSoup(response.text , "html.parser")

items = soup.find_all("li")

data=[]
for items in items : 
    text = items.text.strip()
    name , price = text.split("-")
    data.append({"Item" : name , "Price " : price })
    
df = pd.DataFrame(data)

print(df)

df.to_csv("canteen_menu.csv" , index = False )
print ("\n saved to canteen_menu.csv")