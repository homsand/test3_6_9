import pytest,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.get(link)
    # скроллим страницу вниз на всякий случай, чтобы кнопку было видно
    browser.execute_script("window.scrollBy(0,40);")
    # Проверяем существование кнопки Добавить в корзину
    btn=len(browser.find_elements_by_css_selector(".add-to-basket > button"))
    assert btn>0, "Нет кнопки!!!"
    time.sleep(3)
    
