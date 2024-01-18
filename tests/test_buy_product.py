from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

def test_buy_product(set_up):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-loading'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")


    mp = MainPage(driver)   # экземпляр класса MainPage
    mp.choosing_categories()

    cp = CatalogPage(driver)    # экземпляр класса CatalogPage
    cp.product_filter()

    pp = ProductPage(driver)    # экземпляр класса ProductPage
    pp.adding_cart()

    cartp = CartPage(driver)    # экземпляр класса CartPage
    cartp.making_order()

    op = OrderPage(driver)    # экземпляр класса OrderPage
    op.buyer_details()