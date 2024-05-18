import requests

res = requests.get("https://www.google.com")
res.raise_for_status()

print("응답코드 : " + str(res.status_code))
print(res.text)

# with open("google.html", "w", encoding="utf8") as f:
# 	f.write(res.text)