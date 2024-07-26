from selenium import webdriver
from selenium.webdriver.chrome.service import Service
web = 'https://www.audible.com/cat/Mystery-Thriller-Suspense-Audiobooks/18574597011'



path = "C:\Users\User\Desktop\DATA SETS\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=Service)
driver.get(web)