import requests
from bs4 import BeautifulSoup
import lxml

url_dnevni = 'https://horoskopius.com/dnevni-horoskop/ovan'
url_nedeljni = "https://horoskopius.com/nedeljni-horoskop/ovan"
url_mesecni = "https://horoskopius.com/mesecni-horoskop/ovan"
url_godisnji = "https://horoskopius.com/godisnji-horoskop/ovan"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "sr-YU"
}

r_d = requests.get(url_dnevni, headers=headers)
r_n = requests.get(url_nedeljni, headers=headers)
r_m = requests.get(url_mesecni, headers=headers)
r_g = requests.get(url_godisnji, headers=headers)

soup = BeautifulSoup(r_d.text, "lxml")
soupG = BeautifulSoup(r_g.text, "lxml")
# print(soup.prettify())


name = soupG.select_one(selector=".article-details").getText()
name = name.strip()
print(name)

