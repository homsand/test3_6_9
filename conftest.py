import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language.")

@pytest.fixture(scope="function")
def browser(request):
    # считываем язык из командной строки
    user_language = request.config.getoption("language")   
    # устанавливаем язык браузера
    options=Options()    
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print("\nstart browser for test..")
    browser=webdriver.Chrome(options=options)
            
    yield browser
    print("\nquit browser..")

    browser.quit()
