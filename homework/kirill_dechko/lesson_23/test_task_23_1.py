import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
@allure.feature('Opening the browser')
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.feature('Put item in cart')
def test_add_to_cart(driver):
    tel = 'Samsung galaxy s6'
    driver.get('https://www.demoblaze.com/index.html')
    tel_elem_xpath = f"//*[text()='{tel}']"
    tel_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, tel_elem_xpath))
    )
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(tel_elem).key_up(Keys.CONTROL).perform()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_button_xpath = "//*[@onclick='addToCart(1)']"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_button_xpath))
    )
    add_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cartur']"))
    )
    cart.click()
    cart_value = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//td[text()='{tel}']"))
    )
    assert cart_value.text == tel
