import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    approval_button = "//button[@class='e4uhfkv0 css-1lxdbiq e4mggex0']"    # согласие с использованием cookie
    min_price = "(//input[@name='input-min'])[2]"   # поле минимальная цена
    max_price = "(//input[@name='input-max'])[2]"   # поле максимальная цена
    monitor_brand = "//input[@id='aoc']"    # выбор бренда монитора
    monitor_diagonal = "//input[@id='2771_162']"    # выбор диагонали монитора
    monitor_resolution = "//input[@id='2718_1621920x1080']"  # выбор разрешения монитора
    type_matrix = "//input[@id='11561_162']"    # типа матрицы монитора
    update_frequency = "//input[@id='10673_162240d1gts']"   # выбор частоты обновления монитора
    found_product = "(//a[@href='/product/monitor-aoc-23-8-gaming-24g2zu-tn-1920x1080-350cd-m2-16-9-1560518/'])[2]"
    # отсортированный товар согласно фильтрам
    catalog_price = "//span[@class='e1j9birj0 e106ikdt0 app-catalog-p2oaao e1gjr6xo0']"
    # стоимость отсортированного товара
    price_global = ""   # пустая переменная для создания переменной класса с ценой, будет использоваться для сравнения
    product_global = ""  # пустая переменная для создания переменной класса с наименованием товара,
    # будет использоваться для сравнения

    # Getters

    def get_approval_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.approval_button)))
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.max_price)))

    def get_monitor_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.monitor_brand)))

    def get_monitor_diagonal(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.monitor_diagonal)))

    def get_monitor_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.monitor_resolution)))

    def get_type_matrix(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.type_matrix)))

    def get_update_frequency(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.update_frequency)))

    def get_found_product(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.found_product)))

    def get_catalog_price(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.catalog_price)))

    # Actions

    def click_approval_button(self):    # клик кнопки согласия с использованием cookie,
        # т.к. закрывает видимость фильтров
        self.get_approval_button().click()
        print("click approval button")
    def input_min_price(self, amount):  # ввод данных в поле минимальная цена
        self.get_min_price().clear()
        self.get_min_price().send_keys(amount)
        print("Input min price")

    def input_max_price(self, amount):  # ввод данных в поле максчимальная цена
        self.get_max_price().clear()
        time.sleep(2)   # задержка в 2 секунды и второй метод клеар, т.к. при автоматическом удалении стандартной цены
        # страница обновляется
        self.get_max_price().clear()
        self.get_max_price().send_keys(amount)
        print("Input max price")

    def click_monitor_brand(self):  # выбор марки монитора
        self.get_monitor_brand().click()
        print("Click monitor brand")

    def click_monitor_diagonal(self):   # выбор диагонали монитора
        self.get_monitor_diagonal().click()
        print("Click monitor diagonal")

    def click_monitor_resolution(self): # выбор разрешения монитора
        self.get_monitor_resolution().click()
        print("Click monitor resolution")

    def click_type_matrix(self):    # выбор матрицы монитора
        self.get_type_matrix().click()
        print("Click type matrix")

    def click_update_frequency(self):   # выбор частоты обновления монитора
        self.get_update_frequency().click()
        print("Click update frequency")

    def save_title_product(self):  # создание перенной класса с наименованием монитора для последующего сравнения
        self.get_found_product().send_keys(Keys.HOME)
        product_title = self.get_found_product()
        CatalogPage.product_global = product_title.text
        print(f"Наименование монитора: {product_title.text}")
        return CatalogPage.product_global

    def save_price_product(self):   # # создание перенной класса с ценой для последующего сравнения
        product_price = self.get_catalog_price()
        CatalogPage.price_global = product_price.text
        print(f"Стоимость монитора: {CatalogPage.price_global}")
        return CatalogPage.price_global

    def click_found_product(self):  # клик по отсортированному товару
        self.get_found_product().click()
        print("Click found product")

    # Methods

    def product_filter(self):
        self.get_current_url()  # url страницы
        self.click_approval_button()
        self.input_min_price(20000)
        self.input_max_price(30000)
        self.click_monitor_brand()
        self.click_monitor_diagonal()
        self.click_monitor_resolution()
        self.click_type_matrix()
        self.click_update_frequency()
        self.save_title_product()
        self.save_price_product()
        self.click_found_product()
        self.get_screenshot()

