import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver = "D:\Git\ElaYJ_ws\Study_Extra\chromedriver-win64\chromedriver.exe"

# browser = webdriver.Chrome(chrome_driver)
# browser.get("https://www.naver.com")

service = Service(executable_path=chrome_driver)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
browser.get("https://www.naver.com")

# 브라우저가 로딩될 때까지 기다리는 방법
browser.implicitly_wait(time_to_wait=5) # 암묵적 대기, 해당 시간만큼 대기
time.sleep(5) # 무작정 대기