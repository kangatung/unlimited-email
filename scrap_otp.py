from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def syarat():
    service = Service(executable_path="/path/to/chromedriver")
    driver = webdriver.Chrome(service=service)

    url = 'https://temporary-phone-number.com/Denmark-Phone-Number/4593705752'
    driver.get(url)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    global data
    data = soup.find_all(class_='btn1')[1].get_text()

def kode_otp():
    otp = data
    return otp


    