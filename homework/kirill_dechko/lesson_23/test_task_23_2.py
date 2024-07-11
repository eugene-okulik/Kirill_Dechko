import time

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


@allure.feature('Compare function')
def test_compare_function(driver):
    product_id = 14
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product_name = driver.find_element(By.XPATH, f"//div[@data-product-id='{product_id}']")
    action = ActionChains(driver)
    action.move_to_element(first_product_name).perform()
    compare_elem_xpath = f"//*[@class='action tocompare' and contains(@data-post, '{product_id}')]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, compare_elem_xpath))
    )
    compare_elem = driver.find_element(By.XPATH, compare_elem_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(first_product_name).click(compare_elem).perform()
    elem_in_compare_xpath = f"//ol[@id='compare-items']//a[contains(@data-post,'product\":\"{product_id}')]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, elem_in_compare_xpath))
    )
    comparing_elem_2 = driver.find_element(By.XPATH, elem_in_compare_xpath)
    assert comparing_elem_2.is_displayed()
