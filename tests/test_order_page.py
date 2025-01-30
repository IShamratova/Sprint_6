import allure
import pytest
from selenium import webdriver
from data.main_page_data import MainPageData
from data.order_page_data import OrderPageData
from pages.main_page import MainPage
from pages.order_page import OrderPage


# Проверка заказа самоката
class TestScooterOrder:
    driver = None

    @classmethod
    @allure.description('Открытие браузера Firefox')
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

        # раскрытие окна драйвера
        cls.driver.maximize_window()

        # открытие страницы тестового стенда
        cls.driver.get(MainPageData.BASE_URL)

    @pytest.mark.parametrize(
        'first_name_text, last_name_text, address_text, station_metro_text, phone_number, delivery_date, comment_courier_text', [
            [
                OrderPageData.FIRST_NAME_TEXT_1,
                OrderPageData.LAST_NAME_TEXT_1,
                OrderPageData.ADDRESS_TEXT_1,
                OrderPageData.STATION_METRO_TEXT_1,
                OrderPageData.PHONE_NUMBER_1,
                OrderPageData.DELIVERY_DATE_1,
                OrderPageData.COMMENT_COURIER_TEXT_1
            ],
            [
                OrderPageData.FIRST_NAME_TEXT_2,
                OrderPageData.LAST_NAME_TEXT_2,
                OrderPageData.ADDRESS_TEXT_2,
                OrderPageData.STATION_METRO_TEXT_2,
                OrderPageData.PHONE_NUMBER_2,
                OrderPageData.DELIVERY_DATE_2,
                OrderPageData.COMMENT_COURIER_TEXT_2
            ]
        ],
        ids = [
            "First Order Test Case",
            "Second Order Test Case"
        ]
    )

    @allure.title('Заказ самоката')
    def test_scooter_order(
            self,
            first_name_text,
            last_name_text,
            address_text,
            station_metro_text,
            phone_number,
            delivery_date,
            comment_courier_text
    ):
        # создание объектов
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        # поиск кнопки «Заказать» и клик по ней
        main_page.click_order_button()

        # ввод данных в окне «Для кого самокат»
        order_page.set_personal_info(
            first_name_text, last_name_text, address_text, station_metro_text, phone_number
        )

        # ввод данных в окне «Про аренду»
        order_page.set_order_info(
            delivery_date, comment_courier_text
        )

        # проверка оформления заказа
        order_page.check_order()

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()

