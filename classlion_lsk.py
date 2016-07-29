import requests
from bs4 import BeautifulSoup

yourid=input("아이디를 입력하세요 : ")
yourpwd=input("비밀번호를 입력하세요 : ")
session=requests.Session()

r=session.get("http://class.likelion.net/users/sign_in")

html=BeautifulSoup(r.text,"html.parser")
token=html.input.next_sibling["value"]
params={'user[email]':yourid ,'user[password]':yourpwd,'authenticity_token':token}
r=session.post("http://class.likelion.net/users/sign_in",params)

r=session.get("http://class.likelion.net")
print(r.text)
