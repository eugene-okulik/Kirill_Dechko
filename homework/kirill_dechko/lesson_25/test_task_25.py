import os
import random

from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

subjects = ['Maths', 'Arts', 'Physics']
hobbies_checkbox = ['hobbies-checkbox-1', 'hobbies-checkbox-2', 'hobbies-checkbox-3']
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Ru CV QA Engineer Kirill Dechko.docx')
home_path = os.path.dirname(os.path.dirname(base_path))
test_file_path = os.path.join(home_path, 'kirill_dechko', 'lesson_22_selenium', 'CV_Dechko.docx')
states = ['NCR']
cities = ['Delhi', 'Noida', 'Gurgaon']


def test_1_form_fall_athentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="username").fill("tom")
    page.get_by_role("textbox", name="password").fill("tomsmith")
    page.get_by_role("button", name="Login").click()
    fall_massage = page.locator("//div[@class='flash error']")
    expect(fall_massage).to_contain_text("Your username is invalid!")


def test_submit_button(page: Page):
    # Предварительные данные
    fake_f_name = fake.first_name()
    fake_l_name = fake.last_name()
    fake_email = fake.email()
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
    page.goto("https://demoqa.com/automation-practice-form")
    # Заполняем поля
    page.fill("#firstName", fake_f_name)  # "#firstName"-селектор, который указывает на элемент с id="firstName"
    page.fill("#lastName", fake_l_name)
    page.fill("#userEmail", fake_email)
    page.click("//*[@class='custom-control-label' and text()='Male']")
    page.fill("#userNumber", mob_num)
    page.click("#dateOfBirthInput")
    page.select_option(".react-datepicker__month-select", month)
    page.select_option(".react-datepicker__year-select", str(year_my))
    page.click(f".react-datepicker__day--0{day}")
    page.fill("#subjectsInput", subject)
    page.keyboard.press("Enter")
    page.check(f"label[for={hobby}]")
    page.fill("#currentAddress", fake_address)
    page.click("#state")
    page.fill("#react-select-3-input", state)
    page.keyboard.press("Enter")
    page.click("#city")
    page.fill("#react-select-4-input", city)
    page.keyboard.press("Enter")
    page.click("#submit")
