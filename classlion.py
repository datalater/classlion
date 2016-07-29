#출처: https://kazuar.github.io/scraping-tutorial/

import requests
from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup

USERNAME = "the7mincheol@naver.com"
PASSWORD = "24901402"

login_url = "http://class.likelion.net/users/sign_in/?next=/"
url = "http://class.likelion.net/home/mypage/950"

session_requests = requests.session()

# Get login crsf token
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

# Create payload
payload = {
    "user[email]": USERNAME,
    "user[password]":PASSWORD,
    "authenticity_token":authenticity_token
}

# Perform login
result = session_requests.post(
    login_url,
    data = payload,
    headers = dict(referer=login_url)
)

# Scrape url
result = session_requests.get(
    url,
    headers = dict(referer=url)
)
html = urlopen(url)
bsObj = BeautifulSoup(html)
print(bsObj.find("a", href="/href/contact").get_text())


