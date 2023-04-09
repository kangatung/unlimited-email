from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from scrap_otp import syarat, kode_otp

def chrome_driver():
    #chrome driver
    global nama, akun
    nama = 'mastung' + str(x)
    akun = nama + '@mail2cool.com'

    service = Service(executable_path="/path/to/chromedriver")
    global driver
    driver = webdriver.Chrome(service=service)
    url = 'https://www.mail2world.com/v1/sig/'
    driver.get(url)

def page_1():
    #nama_depan
    driver.find_element(By.NAME, 'first-name').send_keys('abdul')
    #nama_belakang
    driver.find_element(By.NAME, 'last-name').send_keys('jalal')
    #username
    driver.find_element(By.ID, 'user-name').send_keys(nama)
    #pilih_domain
    driver.find_element(By.XPATH,'//*[@id="menudomains"]/option[6]').click()
    #sandi
    driver.find_element(By.ID, 'password').send_keys('@Kiyangkong123')
    #kon_sandi
    driver.find_element(By.ID, 'confirm-password').send_keys('@Kiyangkong123')
    #button_next
    driver.find_element(By.ID, 'signup_s1btn').send_keys(Keys.ENTER)
    time.sleep(4)

def page_2():
    #phone_number
    driver.find_element(By.ID, 'phone').send_keys('93705752')
    #req_code
    driver.find_element(By.ID,'signup_s2btn').send_keys(Keys.ENTER)
    time.sleep(10)

def page_3():
    #scrap kode otp gmail
    syarat()
    my_otp = kode_otp()
    time.sleep(10)
    #otp
    driver.find_element(By.ID,'verification-code').send_keys(my_otp)
    time.sleep(10)
    #req_code
    driver.find_element(By.ID,'signup_s3btn').send_keys(Keys.ENTER)
    time.sleep(10)

def page_4():
    #month
    driver.find_element(By.XPATH,'//*[@id="menudmonth"]/option[3]').click()
    #day
    driver.find_element(By.ID,'date').send_keys('21')
    #year
    driver.find_element(By.ID,'year').send_keys('2003')
    #button
    driver.find_element(By.ID,'signup_s4btn').send_keys(Keys.ENTER)
    #end program
    time.sleep(5)
    driver.quit()

def main():
    chrome_driver()
    page_1()
    page_2()
    page_3()
    page_4()
    print(akun)

x = int(input('masukkan nilai x: '))

try:
    main()
except:
    try:
        x = x + 1
        main()
    except:
        x = x + 2
        main()





