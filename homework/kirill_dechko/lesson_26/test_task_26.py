import re

from playwright.async_api import BrowserContext
from playwright.sync_api import Page, expect


def test_massage_after_confirm_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())  # Этот шаг устанавливает обработчик для диалоговых окон
    # (alert, confirm, prompt). В данном случае, когда появляется alert окно, оно автоматически закрывается нажатием
    # кнопки "OK".
    page.click("//*[@class='a-button' and text()='Click']")  # жмем на кнопку
    expect(page.locator("//*[@class='result-text']").get_by_text(re.compile('Ok')))  # проверяем что элемент содержит Ok


def test_massage_on_a_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    new_page_button = page.locator("//*[@id='new-page-button']")  # находим кнопку
    expect(new_page_button).to_be_enabled()  # проверяем что она активна
    with context.expect_page() as new_page_event:
        new_page_button.click()  # нажимаем на кнопку и ожидаем открытие новой вкладки
    new_page = new_page_event.value  # получение новой вкладки
    new_page.wait_for_load_state()  # ожидание полной прогрузки
    text_on_new_tab = new_page.locator("//*[@id ='result-text']")  # находим элемент на новой вкладке
    expect(text_on_new_tab).to_contain_text("I am a new page in a new tab")  # проверяем его текст
    page.bring_to_front()  # возврат на первую вкладку
    expect(new_page_button).to_be_enabled()  # проверяем что кнопка активна


def test_button_change_color(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    visible_after_button = page.locator("//*[@id ='visibleAfter']")  # ждем отображение кнопки
    expect(visible_after_button).to_be_visible()  # проверяем что кнопка видима
    button = page.locator("//*[@id ='colorChange']")  # находим кнопку
    expect(button).to_have_css("color", "rgb(220, 53, 69)")  # проверяем цвет кнопки
