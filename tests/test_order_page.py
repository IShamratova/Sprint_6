import allure
import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from data.base_page_data import BasePageData
from data.order_page_data import OrderPageData


# Проверка заказа самоката
class TestOrderPage:
    driver = None

    @classmethod
    @allure.description('Открытие браузера Firefox')
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

        # раскрытие окна драйвера
        cls.driver.maximize_window()

        # открытие страницы тестового стенда
        cls.driver.get(BasePageData.BASE_URL)

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
    def test_open_input_data_order_page(
            self,
            first_name_text,
            last_name_text,
            address_text,
            station_metro_text,
            phone_number,
            delivery_date,
            comment_courier_text
    ):
        order_page = OrderPage(self.driver)

        # поиск кнопки «Заказать» и клик по ней
        order_page.click_order_button()

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

