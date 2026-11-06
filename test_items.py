import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket_is_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза 30 секунд, необходимая по условию задания для проверки языка
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину по её уникальному CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка отображается на странице
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице!"
