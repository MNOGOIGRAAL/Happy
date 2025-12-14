import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def test_data():
        return {"full_name": "Аркадий Мартынов",
                "email": "arkady671@mail.ru",
                "current_address": "г.Уфа, Ленина 1, д. 1",
                "permanent_address": "г.Уфа, Пушкина 19, д. 19"
                }

def test_form_text_box(test_data):
        s = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get('https://demoqa.com/text-box')
        time.sleep(3)

        input_full_name = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")
        input_full_name.clear()
        input_full_name.send_keys(test_data["full_name"])

        input_email = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")
        input_email.clear()
        input_email.send_keys(test_data["email"])

        textarea_current_address = driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']")
        textarea_current_address.clear()
        textarea_current_address.send_keys(test_data["current_address"])

        textarea_permanent_address = driver.find_element(By.ID, "permanentAddress")
        textarea_permanent_address.clear()
        textarea_permanent_address.send_keys(test_data["permanent_address"])

        button_submit = driver.find_element(By.ID, 'output')
        button_submit.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='border col-md-12 col-sm-12']")))
        result_name = driver.find_element(By.ID, "name").text
        result_email = driver.find_element(By.ID, "email").text
        result_current_address = driver.find_element(By.ID, "currentAddress").text
        result_permanent_address = driver.find_element(By.ID, "permanentAddress").text

        assert f"Name:{test_data['full_name']}" == result_name
        assert f"Email:{test_data['email']}" == result_email
        assert f"Current Address :{test_data['current_address']}" == result_current_address
        assert f"Permananet Address :{test_data['permanent_address']}" == result_permanent_address

        driver.quit()