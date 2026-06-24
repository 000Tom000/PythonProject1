import requests
session = requests.Session()
res = session.get("https://www.baidu.com/")
print(res.text)