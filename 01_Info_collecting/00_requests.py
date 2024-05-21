import requests

print(requests.__version__)

res = requests.get("http://www.google.com")
print(res.raise_for_status())
print("응답코드 : " + str(res.status_code))

# print(res.text)
with open("google.html", "w", encoding="utf8") as f:
	f.write(res.text)