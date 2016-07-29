import requests
from bs4 import BeautifulSoup

yourid="the7mincheol@naver.com"
yourpwd="24901402"
session=requests.Session()

r=session.get("http://class.likelion.net/users/sign_in")

html=BeautifulSoup(r.text,"html.parser")

token2=html.input.next_sibling["type"]
print(token2)
token=html.input.next_sibling["value"]
print(token)

'''
params={'user[email]':yourid ,'user[password]':yourpwd,'authenticity_token':token}
r=session.post("http://class.likelion.net/users/sign_in",params)

r=session.get("http://class.likelion.net")
print(r.text)
'''
