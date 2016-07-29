import requests
from bs4 import BeautifulSoup


#id, pw 미리 입력
yourid="the7mincheol@naver.com"
yourpwd="24901402"

'''
#id, pw input으로 받기
yourid=input("아이디를 입력하세요 : ")
yourpwd=input("비밀번호를 입력하세요 : ")
'''
#리퀘스트에서 세션 객체를 생성
session=requests.Session()

#해당 url을 GET 방식으로 사이트 오픈(세션: 브라우져에서 웹페이지를 여는 것)
r=session.get("http://class.likelion.net/users/sign_in")

#동일 session에서 BeautifulSoup 실시
html=BeautifulSoup(r.text,"html.parser")

#로그인에 필요한 hidden input인 token과 params 데이터 가져오기
token=html.input.next_sibling["value"]
params={'user[email]':yourid ,'user[password]':yourpwd,'authenticity_token':token}

#로그인 url에 POST 방식으로 사이트 오픈
r=session.post("http://class.likelion.net/users/sign_in",params)

try:
  for n in range(1,1229):
    r=session.get("http://class.likelion.net/home/mypage/{0}".format(n))
    html=BeautifulSoup(r.text,"html.parser")

    for luniv in html.find("div", {"class":"user-profile"}).span.stripped_strings:
      print(luniv)
    for lname in html.find("div", {"class":"user-profile"}).a.stripped_strings:
      print(str(n)+" "+lname)
    for lpercent in html.find("p", {"class":"percent"}).stripped_strings:
      print(lpercent)
      print("---------------")
    
except AttributeError:
    print(str(n)+": 존재하지 않는 번호입니다")

try:
  for n in range(1229,1417):
    r=session.get("http://class.likelion.net/home/mypage/{0}".format(n))
    html=BeautifulSoup(r.text,"html.parser")

    for luniv in html.find("div", {"class":"user-profile"}).span.stripped_strings:
      print(luniv)
    for lname in html.find("div", {"class":"user-profile"}).a.stripped_strings:
      print(str(n)+" "+lname)
    for lpercent in html.find("p", {"class":"percent"}).stripped_strings:
      print(lpercent)
      print("---------------")
    
except AttributeError:
    print(str(n)+": 존재하지 않는 번호입니다")
    pass

  
#try, except로 에러 예외처리하기

