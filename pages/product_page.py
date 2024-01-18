
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.catalog_page import CatalogPage



class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_cart = "//button[@data-meta-name='BasketDesktopButton']"  # кнопка оформить заказ
    go_to_cart = "(//button[@class='e4uhfkv0 css-gh3izc e4mggex0'])[1]" # кнопка перейти в корзину
    word_cart = "(//span[contains(text(), 'Корзина')])[2]"
    product_page_title = "//div[@data-meta-name='ProductHeaderLayout__title']/h1"  # название монитора
    product_page_price = "(//span[@data-meta-is-total='notTotal']/span)[1]"   # цена монитора

    # Getters

    def get_product_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.product_page_title)))

    def get_product_page_price(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.product_page_price)))
    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_cart)))

    # Action

    def save_product_page_product_title(self):  # считывание текста с названием монитора
        product_page_product_title = self.get_product_page_title()
        product_page_product_title_text = product_page_product_title.text
        print("save product page product title")
        return product_page_product_title_text

    def save_product_page_product_price(self):  # считывание текста со стоимостью монитора
        product_page_product_price = self.get_product_page_price()
        product_page_product_price_text = product_page_product_price.text
        print("save product page product price")
        return product_page_product_price_text

    def click_button_card(self):    # нажатие кнопки в корзину
        self.get_button_cart().click()
        print("Click button card")

    def click_go_to_cart(self):  # нажатие кнопки в коризну
        self.get_go_to_cart().click()
        print("Click go to cart")

    # Methods
    def adding_cart(self):
        self.get_current_url()
        self.save_product_page_product_price()
        self.assert_product_title(CatalogPage.product_global, self.save_product_page_product_title())   # сравнение
        # названия монитора из каталога и в карточке товара
        self.assert_product_price(CatalogPage.price_global, self.save_product_page_product_price())  # сравнение
        # стоимости монитора из каталога и в карточке товара
        self.click_button_card()
        self.click_go_to_cart()
        self.assert_world(self.get_word_cart(), "Корзина")  # сравнение по слову Корзина,
        # для подтверждения перехода
        self.get_screenshot()