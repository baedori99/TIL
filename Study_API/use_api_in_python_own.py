import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv

load_dotenv()


def search_naver_news(word):

    client_id = os.getenv("NAVER_CLIENT_ID")
    client_key = os.getenv("NAVER_CLIENT_KEY")
    encrypt_text = urllib.parse.quote(word)

    # client_id = str(client_id)
    # client_key = str(client_key)

    url = (
        "https://openapi.naver.com/v1/search/shop?query="
        + encrypt_text
        + "&display=20&exclude=used:rental"
    )  # "https://openapi.naver.com/v1/search/news?query=" + encrypt_text
    req = urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_key)
    response = urllib.request.urlopen(req)
    response_code = response.getcode()

    if response_code == 200:
        response_output = response.read().decode("utf-8")
    else:
        response_output = "Error" + response_code

    return response_output


output = search_naver_news("뉴진스")
print(json.loads(output))
