import datetime
class Base():

    def __init__(self, driver):
        self.driver = driver    #хранит драйвер чтобы всё работало



    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")  # присваивает время и дату скриншоту
        self.driver.save_screenshot(f".\\screen\\screenshot {now_date}.png")    # сохраняем скриншоты в директорию скриншот

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_world(self, getter, word):
        value_getter = getter.text
        assert value_getter == word
        print("Good value word")

    """Method assert price"""

    def assert_product_price(self, price_1, price_2):
        assert price_1 == price_2
        print(f"Стоимость равна: {price_1} = {price_2}")

    """Method assert product title"""

    def assert_product_title(self, title_1, title_2):
        assert title_1 == title_2
        print(f"Наименование равно: {title_1} = {title_2}")