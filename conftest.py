import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем опцию --language со значением по умолчанию 'en'
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Считываем язык из командной строки
    user_language = request.config.getoption("--language")
    
    options = Options()
    # Устанавливаем язык для браузера
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })
    
    print(f"\nstart browser for test.. with language: {user_language}")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()
