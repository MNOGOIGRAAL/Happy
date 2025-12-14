import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://ya.ru'

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(BASE_URL)
time.sleep(2)

search_fiend = driver.find_element(By.ID, value="text")
search_fiend.send_keys("mail")
time.sleep(2)

search_fiend.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

mail_link = driver.find_element(By.XPATH, '//a[contains(normalize-space(), "Mail: Почта, Облако,")]')
mail_link.click()
time.sleep(5)

handles = driver.window_handles
print(handles)
print(f"Всего вкладок {len(handles)}")
driver.switch_to.window(handles[1])

log_mail = driver.find_element(By.XPATH, "//a[text()='Войти']")
log_mail.click()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.ag-popup__frame__layout__iframe")))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Имя ящика']")))
input_field = driver.find_element(By.XPATH, "//input[@placeholder='Имя ящика']")
input_field.send_keys("TestMail")

button_enter = driver.find_element(By.XPATH, "//button[@data-test-id='continue-button']")
button_enter.click()
time.sleep(5)

driver.quit()