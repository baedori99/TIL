import urllib.request
import os

client_id = "인증 아이디"#os.getenv("NAVER_CLIENT_ID")
client_secret = "인증 비밀번호"#os.getenv("NAVER_CLIENT_KEY")
encText = urllib.parse.quote("뉴진스")
url = "https://openapi.naver.com/v1/search/news?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    print(response_body.decode("utf-8"))
else:
    print("Error Code:" + rescode)
