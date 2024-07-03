import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.support.wait import WebDriverWait

languages = ['Python', 'JavaScript', 'C#', 'Java', 'Ruby']


@pytest.fixture()
@allure.feature('Opening the browser')
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.feature('Select a language')
def test_language_chose(driver):
    language = random.choice(languages)
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='id_choose_language']")))
    language_input.send_keys(language)
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                    "//input[@id='submit-id-submit']")))
    submit_button.click()
    chosen_language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='result-text']")))
    assert chosen_language.text == language


@allure.feature('Greeting phrase check')
def test_hello_elem(driver):
    hello_str = "Hello World!"
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='start']/button")))
    start_button.click()
    find_hello = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
    assert find_hello.text == hello_str
