import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.catalog_page import CatalogPage


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_page_title = "//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']"  # название товара в корзине
    # cart_page_price = "//span[@class='e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0']"  # стоимость товара в корзине
    warranty_extension = "(//div[@data-meta-name='ToggleButtonGroup']/div)[1]"  # полис продления гарантии +
    testing_monitor = "(//div[@data-meta-name='AdditionalService']/div/span[@class='e11v1gn60 css-389ojc elcxude0'])[6]"
    # доп. услуга тестирование монитора
    price_monitor = "(//span[@class='e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0'])[1]"   # название товара в корзине
    price_warranty = "(//span[@data-meta-price='2400']/span)[3]"    # стоимость полиса продления гарантии
    price_testing = "(//span[@class ='e1j9birj0 e106ikdt0 css-xbfpj5 e1gjr6xo0'])[9]"   # стоимость тестирования монитора
    price_final = "//span[@class='e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0']"   # итоговая стоимость монитора с доп услугами
    button_registration = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']" # кнопка перейти к оформлению
    word_order = "//span[contains(text(), 'Оформление заказа')]"
    # warranty_extension_text = "(//span[@class='e1ys5m360 e106ikdt0 css-xbfpj5 e1gjr6xo0'])[3]"
    # testing_text = "(//span[@class='e1ys5m360 e106ikdt0 css-xbfpj5 e1gjr6xo0'])[9]"

    final_price_global = "" # переменная класса

    # Getters

    def get_cart_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_page_title)))

    # def get_cart_page_price(self):
        # return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_page_price)))

    def get_warranty_extension(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.warranty_extension)))

    def get_testing_monitor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.testing_monitor)))

    def get_price_monitor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_monitor)))

    def get_price_warranty(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_warranty)))

    def get_price_testing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_testing)))

    def get_price_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_final)))

    def get_button_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_registration)))

    def get_word_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_order)))

    # Action

    def save_cart_page_title(self): # название товара в корзине
        cart_page_product_title = self.get_cart_page_title()
        cart_page_product_title_text = cart_page_product_title.text
        print("save cart page title")
        return cart_page_product_title_text


    def save_price_monitor(self):   # стоимость товара в корзине
        cart_page_product_price = self.get_price_monitor()
        cart_page_product_price_text = cart_page_product_price.text
        print("cart page product price")
        return cart_page_product_price_text


    def save_cart_page_final_price(self):  # переменная класса с итоговой стоимостью
        cart_page_product_final_price = self.get_price_final()
        CartPage.final_price_global = cart_page_product_final_price.text
        print(f"Итоговая стоимость товара: {CartPage.final_price_global}")
        return CartPage.final_price_global

    def click_warranty_extension(self):  # выбор полиса продления гарантии
        self.get_warranty_extension().click()
        print("Click warranty extension")

    def click_testing_monitor(self):    # выбор тестирования монитора
        self.get_testing_monitor().click()
        print("Click testing monitor")

    def assert_final_price(self):   # сравнение подсчета итоговой стоимости
        p_monitor = self.get_price_monitor().text   # стоимость монитора
        p_warranty = self.get_price_warranty().text  # стоимость полиса продления гарантии
        p_testing = self.get_price_testing().text   # стоимость тестирования монитора
        p_final = self.get_price_final().text   # итоговая стоимость рассчитанная автоматически
        amount_product = int(p_monitor.replace(" ", "")) + int(p_warranty) + int(p_testing)
        assert amount_product == int(p_final.replace(" ", ""))
        print("Assert final price good")


    def click_button_registration(self):    # переход к оформлению заказа
        self.get_button_registration().click()
        print("Click button registration")


    # Methods

    def making_order(self):
        self.get_current_url()
        self.assert_product_title(CatalogPage.product_global, self.save_cart_page_title())
        self.assert_product_price(CatalogPage.price_global, self.save_price_monitor())
        self.click_warranty_extension()
        time.sleep(2)   # задержка в 2 секунды, т.к. локаторы доп. продуктов динамичные
        self.click_testing_monitor()
        self.assert_final_price()
        self.save_cart_page_final_price()
        self.click_button_registration()
        self.assert_world(self.get_word_order(), "Оформление заказа")   # подтверждение перехода на страницу
        # оформления заказа
        self.get_screenshot()