import time
import os
import pytest
import allure
import random

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()
genders = ['gender-radio-1', 'gender-radio-2', 'gender-radio-3']
subjects = ['Maths', 'Arts', 'Physics']
hobbies_checkbox = ['hobbies-checkbox-1', 'hobbies-checkbox-2', 'hobbies-checkbox-3']
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Ru CV QA Engineer Kirill Dechko.docx')
home_path = os.path.dirname(os.path.dirname(base_path))
test_file_path = os.path.join(home_path, 'kirill_dechko', 'lesson_22_selenium', 'CV_Dechko.docx')
states = ['NCR']
cities = ['Delhi', 'Noida', 'Gurgaon']


@pytest.fixture()
@allure.feature('Opening the browser')
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    # chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()


@allure.feature('Filling First name field')
def test_first_name_fild(driver):
    fake_name = fake.name()
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.ID, "firstName")
    search_input.send_keys(fake_name)
    assert search_input.get_attribute("value") == fake_name


@allure.feature('Filling Second name field')
def test_second_name_fild(driver):
    fake_name = fake.name()
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.ID, "lastName")
    search_input.send_keys(fake_name)
    assert search_input.get_attribute("value") == fake_name


@allure.feature('Filling Email field')
def test_email_fild(driver):
    fake_email = fake.email()
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.ID, "userEmail")
    search_input.send_keys(fake_email)
    assert search_input.get_attribute("value") == fake_email


@allure.feature('Choosing Gender')
def test_gender_fild(driver):
    random_gender = random.choice(genders)
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.ID, random_gender)
    driver.execute_script("arguments[0].click();", search_input)
    assert search_input.is_selected()


@allure.feature('Filling Mobile Number field')
def test_phone_fild(driver):
    mob_num = str(random.randint(1000000000, 2000000000))
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Mobile Number"]')
    search_input.send_keys(mob_num)
    assert search_input.get_attribute("value") == mob_num


@allure.feature('Filling in the Date field')
def test_date_fild(driver):
    day = 28
    month = 'May'
    year_my = 1982
    date = f"{day} {month} {year_my}"
    driver.get("https://demoqa.com/automation-practice-form")
    search_input = driver.find_element(By.ID, 'dateOfBirthInput')
    search_input.click()
    # driver.implicitly_wait(1000)
    month_select = driver.find_element(By.XPATH, "//*[contains(@class,'month-select')]")
    month_select.click()
    may_select = driver.find_element(By.XPATH, f"//option[text()='{month}']")
    may_select.click()
    year_select = driver.find_element(By.XPATH, "//*[contains(@class,'year-select')]")
    year_select.click()
    year = driver.find_element(By.XPATH, f"//option[text()='{year_my}']")
    year.click()
    date_select = driver.find_element(By.XPATH, f"//*[contains(@class,'react-datepicker') and text()='{day}']")
    date_select.click()
    assert search_input.get_attribute("value") == date


@allure.feature('Filling the Subjects field')
def test_subject_fild(driver):
    subject = random.choice(subjects)
    driver.get("https://demoqa.com/automation-practice-form")
    # Ожидание загрузки элемента ввода и ввод текста из subject
    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='subjectsInput']")))
    subject_input.send_keys(subject)
    assert subject_input.is_displayed(), f"Subject {subject} is not displayed"


@allure.feature('Selecting a checkbox')
def test_hobby_field(driver):
    hobby = random.choice(hobbies_checkbox)
    driver.get("https://demoqa.com/automation-practice-form")
    hobby_label = driver.find_element(By.XPATH, f"//label[@for='{hobby}']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_label)
    hobby_label.click()
    hobby_checkbox = driver.find_element(By.XPATH, f"//input[@id='{hobby}']")
    assert hobby_checkbox.is_selected(), f"Checkbox {hobby} is not selected."


@allure.feature('Checking file selection')
def test_add_file_button(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    input_file = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
    input_file.send_keys(test_file_path)
    driver.implicitly_wait(5)
    uploaded_file_name = input_file.get_attribute('value')
    assert 'CV_Dechko.docx' in uploaded_file_name, \
        f"Имя файла не соответствует ожидаемому. Ожидалось: 'CV_Dechko.docx', найдено: {uploaded_file_name}"


@allure.feature('Filling in the Current Address field')
def test_address_fild(driver):
    fake_address = fake.address()
    driver.get("https://demoqa.com/automation-practice-form")
    text_fild = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Current Address']")))
    text_fild.send_keys(fake_address)
    uploaded_fild = text_fild.get_attribute('value')
    assert fake_address in uploaded_fild


@allure.feature('Filling in the Staff field')
def test_state_field(driver):
    state = random.choice(states)
    driver.get("https://demoqa.com/automation-practice-form")
    state_dropdown = driver.find_element(By.XPATH, "//div[text()='Select State']")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
    state_dropdown.click()
    state_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    state_input.send_keys(state)
    state_input.send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, f"//div[text()='{state}']").is_displayed()


@allure.feature('Filling in the City field')
def test_city_field(driver):
    city = random.choice(cities)
    state = random.choice(states)
    driver.get("https://demoqa.com/automation-practice-form")
    state_dropdown = driver.find_element(By.XPATH, "//div[text()='Select State']")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
    state_dropdown.click()
    state_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    state_input.send_keys(state)
    state_input.send_keys(Keys.ENTER)
    city_dropdown = driver.find_element(By.XPATH, "//div[text()='Select City']")
    city_dropdown.click()
    city_input = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
    city_input.send_keys(city)
    city_input.send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, f"//div[text()='{city}']").is_displayed()


@allure.feature('Filling out and submitting the form')
def test_submit_button(driver):
    # Предварительные данные
    fake_f_name = fake.first_name()
    fake_l_name = fake.last_name()
    fake_email = fake.email()
    random_gender = random.choice(genders)
    mob_num = str(random.randint(1000000000, 2000000000))
    day = 28
    month = 'May'
    year_my = 1982
    subject = random.choice(subjects)
    hobby = random.choice(hobbies_checkbox)
    fake_address = fake.address()
    state = random.choice(states)
    city = random.choice(cities)
    # Открываем страницу в браузере
    driver.get("https://demoqa.com/automation-practice-form")
    # Заполняем поля
    state_dropdown = driver.find_element(By.XPATH, "//div[text()='Select State']")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
    search_input = driver.find_element(By.ID, "firstName")
    search_input.send_keys(fake_f_name)
    search_input = driver.find_element(By.ID, "lastName")
    search_input.send_keys(fake_l_name)
    search_input = driver.find_element(By.ID, "userEmail")
    search_input.send_keys(fake_email)
    search_input = driver.find_element(By.ID, random_gender)
    driver.execute_script("arguments[0].click();", search_input)
    search_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Mobile Number"]')
    search_input.send_keys(mob_num)
    search_input = driver.find_element(By.ID, 'dateOfBirthInput')
    search_input.click()
    month_select = driver.find_element(By.XPATH, "//*[contains(@class,'month-select')]")
    month_select.click()
    may_select = driver.find_element(By.XPATH, f"//option[text()='{month}']")
    may_select.click()
    year_select = driver.find_element(By.XPATH, "//*[contains(@class,'year-select')]")
    year_select.click()
    year = driver.find_element(By.XPATH, f"//option[text()='{year_my}']")
    year.click()
    date_select = driver.find_element(By.XPATH, f"//*[contains(@class,'react-datepicker') and text()='{day}']")
    date_select.click()
    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='subjectsInput']")))
    subject_input.send_keys(subject)
    subject_input.send_keys(Keys.ENTER)
    hobby_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//label[@for='{hobby}']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_label)
    hobby_label.click()
    input_file = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
    input_file.send_keys(test_file_path)
    driver.implicitly_wait(5)
    input_file.get_attribute('value')
    text_fild = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Current Address']")))
    text_fild.send_keys(fake_address)
    text_fild.get_attribute('value')
    state_dropdown = driver.find_element(By.XPATH, "//div[text()='Select State']")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
    state_dropdown.click()
    state_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    state_input.send_keys(state)
    state_input.send_keys(Keys.ENTER)
    city_dropdown = driver.find_element(By.XPATH, "//div[text()='Select City']")
    city_dropdown.click()
    city_input = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
    city_input.send_keys(city)
    city_input.send_keys(Keys.ENTER)
    submit_button = driver.find_element(By.XPATH, "//*[@Id='submit']")
    submit_button.click()
