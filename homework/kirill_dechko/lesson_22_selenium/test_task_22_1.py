import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
@allure.feature('Opening the browser')
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_form_field(driver):
    test_word = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Submit me']")
    search_input.send_keys(test_word)
    search_input.submit()
    result_text = driver.find_element(By.XPATH, "//*[@Id='result-text']")
    assert result_text.text == test_word, "Error, check your text."
    print(result_text.text)
