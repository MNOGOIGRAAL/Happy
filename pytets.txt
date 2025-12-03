from encodings import search_function

from re import search

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://ya.ru')
time.sleep(2)
search_fiend = driver.find_element(By.ID, value="text")
search_fiend.send_keys("mail")
time.sleep(1)
search_fiend.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
mail_link = driver.find_element(By.XPATH, '//a[contains(normalize-space(), "Mail: Почта, Облако,")]')
mail_link.click()
time.sleep(5)
log_mail = driver.find_element(By.XPATH, '//*[@id="mailbox"]/div[1]/a')
if not log_mail:
    print("Элемент  не найден")
else:
    print("Элемент найден")
log_mail.click()
form_mail = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div')))
input_field = driver.find_element(By.XPATH, '//*[@id="email"]')
input_field.send_keys("cocoon")
time.sleep(1)


driver.quit()