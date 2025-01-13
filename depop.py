import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

headers = {
    'authority': 'webapi.depop.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'depop-device-id': '1fa2a62b-dba0-4459-93de-97a19fa3e607',
    'depop-search-id': 'baa3bde1-c4d8-4c62-b284-b631fd30bf75',
    'depop-session-id': 'c4894499-b58c-4579-a6ce-e8b59e6a299c',
    'origin': 'https://www.depop.com',
    'referer': 'https://www.depop.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

params = {
    'categories': '1',
    'cursor': 'MTJ8MjY0fDE2ODU0NDMxMTY',
    'itemsPerPage': '24',
    'country': 'gb',
    'currency': 'GBP',
    'sort': 'relevance',
}

response = requests.get('https://webapi.depop.com/api/v2/search/products/', params=params, headers=headers)

url = "https://www.depop.com/category/mens/?categoryPath=mens"

xy = []
a1 = []
b1 = []
c1 = []
c2 = []

r = requests.get(url)

sp = bs(r.text,"html.parser")
links = sp.find_all("li",attrs = {"class" : "styles__ProductCardContainer-sc-__sc-13q41bc-7 imvpaW"})

for i in links:
    w = "https://www.depop.com" + i.find("a")["href"]
    #print(w)
    xy.append(w)     
    
#########
 
    r = requests.get(w)
    cd = []

    sp = bs(r.text,"html.parser")
    name = sp.find_all("div",attrs = {"class" : "styles__Layout-sc-__sc-1fk4zep-2 kQytFU"})
    #name = sp.find_all("div",attrs = {"class" : "styles__ContentWrapper-sc-__sc-1fk4zep-3 gfEHsG"})

    for i in name:
        a = i.find("h1",attrs = {"class" : "sc-kDDrLX ProductDetailsStickystyles__ProductTitle-sc-__sc-17vfpzd-1 bmzCVg euvWvH"}).text
        a1.append(a)
        print(a)

        b = i.find("div",attrs = {"class" : "ProductPricestyles__PriceWrapper-sc-__sc-1779phz-0 hvpUkx"}).text
        b1.append(b)
        print(b)

        c = i.find("td",attrs = {"class" : "TableCell-sc-__sc-12y8so1-0 bWenjz"}).text
        c1.append(c)
        print(c)
     
        for d in i.find_all("div",attrs={"class":"styles__ImageContainer-sc-__sc-143ql1a-3 gIOdAg"}):
            e = d.find("img")["src"]
            if e not in cd:

                # print(a)
                # a1.append(a)

                # print(b)
                # b1.append(b)

                # print(c)
                # c1.append(c)

                cd.append(e)

        print(cd)
        c2.append(cd)
    print("\n")

print(len(xy))
print(len(a1))
print(len(b1))
print(len(c1))
print(len(c2))

df = pd.DataFrame({"Product Name":a1,"Product Price":b1,"Product Size":c1,"Product Photo":c2})

print(df)

df.to_csv("depop.csv")