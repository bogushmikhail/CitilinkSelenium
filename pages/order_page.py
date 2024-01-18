import time

from faker import Faker
from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage

faker_ru = Faker("ru_RU")
faker_eng = Faker("en_US")

class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@name='contact-form_firstName']"  # имя в данных пользователя
    last_name = "//input[@name='contact-form_lastName']"    # фамилия в данных пользователя
    number_phone = "//input[@name='contact-form_phone']"    # номер телефона в данных пользователя
    number_phone_second = "//input[@name='contact-form_additionalPhone']"   # второй номер телефона в данных пользователя
    use_data = "(//button[@class='css-1qkge9l ek97e1d0'])[1]"   # кнопка использовать данный пользователя в страховании
    selecting_item = "//button[@class='e4uhfkv0 css-a9m9r e4mggex0']" # кнопка выбора пункта самовывоза
    the_point_of_issue = "(//button[@class='e1tiqnd20 css-18kees1 e4mggex0'][1])"   # выбор пункта выдачи из списка
    payment_method = "//*[contains(text(), 'Банковской картой онлайн')]"    # метод оплаты товара
    email = "//input[@name='contactForCheck_email']"    # электронная почта для получения чека
    email_duplicate = "(//input[@type='text'])[9]"  # почта в данных страхователя
    confirmation_data = "//input[@id='contactPaymentConfirm']"  # подтверждение введенных данных
    order_page_final_price = "(//span[@class='e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0'])[2]"  # итоговая цена
    order_page_title = "(//span[@class='e27li280 e106ikdt0 css-1qo2d1j e1gjr6xo0'])[4]" # название товара
    button_payment = "//button[@class='e1jq023s0 css-cc7j09 e4mggex0']" # кнопка оплатить

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_number_phone_second(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone_second)))

    def get_use_data(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.use_data)))

    def get_selecting_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selecting_item)))

    def get_the_point_of_issue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.the_point_of_issue)))

    def get_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.payment_method)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.email)))

    def get_email_duplicate(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.email_duplicate)))

    def get_confirmation_data(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.confirmation_data)))

    def get_order_page_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_page_final_price)))

    def get_order_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_page_title)))

    def get_button_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_payment)))

    # Action

    def input_first_name(self): # заполнение имени
        self.get_first_name().send_keys(str(faker_ru.first_name()))
        print("Input first name")

    def input_last_name(self):  # заполнение фамилии
        self.get_last_name().send_keys(str(faker_ru.last_name()))
        print("Input last name")

    def input_number_phone(self):   # заполнение номера телефона
        self.get_number_phone().send_keys(faker_ru.msisdn())
        print("Input number phone")

    def input_number_phone_second(self):    # заполнение второго номера телефона
        self.get_number_phone_second().send_keys(faker_ru.msisdn())
        print("Input number phone second")

    def save_order_page_final_price(self):  # сохранение названия товара для сравнения
        order_page_product_final_price = self.get_order_page_final_price()
        order_page_product_final_price_text = order_page_product_final_price.text
        print("save order page final price")
        return order_page_product_final_price_text

    def save_order_page_title(self):    # сохранение цены товара для сравнения
        order_page_product_title = self.get_order_page_title()
        order_page_product_title_text = order_page_product_title.text
        print("save order page title")
        return order_page_product_title_text

    def click_selecting_item(self): # клик кнопка выбор пункта самовывоза
        self.get_selecting_item().click()
        print("Click selecting item")

    def click_the_point_of_issue(self): # выбор пункта выдачи из перечня
        self.get_the_point_of_issue().click()
        print("Input the point of issue")

    def click_payment_method(self): # выбор метода оплаты
        self.get_payment_method().click()
        print("Click payment method")

    def input_email(self):  # заполнение адреса электронной почты
        self.get_email().send_keys(str(faker_eng.first_name() + str(faker_eng.random_int()) + "@yandex.ru"))
        print("Input email")

    def input_email_duplicate(self):    # копирование сгенерированного почтового адреса в поле почты в страховании
        value_email = self.get_email().get_attribute("value")
        self.get_email_duplicate().send_keys(value_email)
        print("Input email duplicate")

    def click_use_data(self):   # нажатие кнопки использоваться данные пользователя в поле страхования
        self.get_use_data().click()
        print("Click use data")

    def click_confirmation_data(self):  # нажатие подтверждения верности введенных данных
        self.get_confirmation_data().click()
        print("Click confirmation data")

    def go_to_button_payment(self): # переход к кнопке оплаты, кнопка становится активна, т.к. все поля заполнены
        self.get_button_payment().send_keys(Keys.END)
        print("go to button payment")

    def buyer_details(self):
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_number_phone()
        self.input_number_phone_second()
        self.assert_product_title(CatalogPage.product_global, self.save_order_page_title())
        self.assert_product_price(CartPage.final_price_global, self.save_order_page_final_price())
        self.click_selecting_item()
        self.click_the_point_of_issue()
        time.sleep(2)   # задержка в 2 секунды из-за того, что сайт не успевает прогрузится после выбора пункта выдачи
        self.click_payment_method()
        self.input_email()
        self.input_email_duplicate()
        self.click_use_data()
        self.click_confirmation_data()
        self.go_to_button_payment()
        self.get_screenshot()




