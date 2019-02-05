from requests import Session, Request
import requests

# s = Session()

client_id = "O5mtOygQdS_DMkJRF8VC" # 개발자센터에서 발급받은 Client ID 값
client_secret = "q8FOGdHj6n" # 개발자센터에서 발급받은 Client Secret 값

headers = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
}

text = 'Hello my name is Jeffrey'

payload = {
    'source':'en',
    'target':'ja',
    'text':text,
}
url = "https://openapi.naver.com/v1/papago/n2mt"

# req  = Request('POST', url , data  = payload, headers = headers)
# prepped = req.prepare()

res = requests.post(url = url, headers = headers , data = payload)
print(res.json())