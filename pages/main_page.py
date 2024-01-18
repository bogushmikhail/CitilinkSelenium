
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    choosing_city = "//button[@class='e1x3msk40 css-wsr9k9 etyxved0']"  # кнопка с названием города на главное странице
    search_city = "(//input[@type='text'])[2]"  # строка поиска города
    found_city = "(//span[@class='css-sl5paq ek3bndn0'])[1]"    # найденный город
    sidebar_button = "//a[@href='/catalog/']"   # sidebar Каталог товаров
    search_bar = "(//input[@type='search'])[2]" # строка поиска Поиск по товарам
    monitors_button = "(//span[@class='e1ys5m360 e106ikdt0 css-rx1cfc e1gjr6xo0']/span)[3]" # найденная категория
    word_catalog = "//h1[contains(text(), 'Мониторы')]"
    # название категории для метода assert

    # Getters

    def get_choosing_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.choosing_city)))

    def get_search_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.search_city)))

    def get_found_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.found_city)))

    def get_sidebar_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.sidebar_button)))

    def get_search_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.search_bar)))

    def get_monitors_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.monitors_button)))

    def get_word_catalog(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.word_catalog)))

    # Actions

    def click_choosing_city(self):  # поиск необходимого города
        self.get_choosing_city().click()
        self.get_search_city().send_keys("Челябинск")
        self.get_found_city().click()
        print("Click choosing city")


    def click_sidebar_button(self): # клик Каталог товаров
        self.get_sidebar_button().click()
        print("Click sidebar button")

    def click_search_bar(self): # клик строка поиска в каталоге товаров
        self.get_search_bar().click()
        print("Click search bar")

    def input_search_bar(self, search_bar): # ввод наименования товара в строку поиска
        self.get_search_bar().send_keys(search_bar)
        print("Input search")

    def click_monitors_button(self):    # клик по найденной категории
        self.get_monitors_button().click()
        print("Click monitors button")



    # Methods

    def choosing_categories(self):
        self.driver.get(self.url)  # обращаемся к юрл сайта ситилинка, инициализируем браузер
        self.driver.maximize_window()  # максимизируем окно браузера
        self.get_current_url()  # url страницы
        self.click_choosing_city()
        self.click_sidebar_button()
        self.click_search_bar()
        self.input_search_bar("Мониторы")
        self.click_monitors_button()
        self.assert_world(self.get_word_catalog(), "Мониторы")  # assert названия категории в которую переходим и
        # слова Мониторы, для подверждения перехода в необходимую категорию
        self.get_screenshot()

