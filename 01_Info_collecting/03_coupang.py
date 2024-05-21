import requests
from bs4 import BeautifulSoup

link = "https://www.coupang.com/np/search?component=&q=%EB%AC%BC%ED%86%B5&channel=user"

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
res = requests.get(link, headers=headers)
print(res)

soup = BeautifulSoup(res.text, 'html.parse')