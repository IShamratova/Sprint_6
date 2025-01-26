from pages.base_page import BaseMethod
from locators.order_page_locators import OrderPageLocator
from data.order_page_data import OrderPageData

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def set_personal_info(
            self,
            first_name_text,
            last_name_text,
            address_text,
            station_metro_text,
            phone_number
    ):
        # явное ожидание для загрузки страницы
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_SCOOTER, 3)

        # поиск поля «Имя», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.FIRST_NAME, first_name_text)

        # поиск поля «Фамилия», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.LAST_NAME, last_name_text)

        # поиск поля «Адрес: куда привезти заказ», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.ADDRESS, address_text)

        # поиск поля «Станция метро», клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.METRO)

        # поиск поля «Станция метро», ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.METRO, station_metro_text)

        # поиск поля станции метро «Парк культуры» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.STATION_METRO)

        # поиск поля «Телефон: на него позвонит курьер», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.PHONE, phone_number)

        # поиск кнопки «Далее» и клик по ней
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.BUTTON_NEXT)

    def set_order_info(
            self,
            delivery_date,
            comment_courier_text
    ):
        # явное ожидание для загрузки страницы
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_RENTAL, 3)

        # Поиск поля «Срок аренды» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.RENTAL_PERIOD)

        # явное ожидание для загрузки выпадающего списка
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.NUMBER_DAYS, 3)

        # поиск поля «трое суток» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.NUMBER_DAYS)

        # поиск поля «Когда привезти самокат», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.WHEN_BRING_SCOOTER, delivery_date)

        # поиск чек-бокса «чёрный жемчуг» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.COLOUR_SCOOTER)

        # поиск поля «Комментарий для курьера», клик по нему и ввод данных
        BaseMethod.set_text_to_field_by_xpath(self, OrderPageLocator.COMMENT_COURIER, comment_courier_text)

        # поиск нижней кнопки «Заказать» и клик по ней
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.LOWER_BUTTON_ORDER)

    def check_order(
            self,

    ):
        # явное ожидание для загрузки всплывающего окна «Хотите оформить заказ?»
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_WANT_ORDER, 3)

        # поиск кнопки «Да» окна «Хотите оформить заказ?» и клик по ней
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.BUTTON_YES)

        # явное ожидание для загрузки всплывающего окна «Заказ оформлен»
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_ORDER_REGISTER, 3)

        # поиск кнопки «Посмотреть статус» окна «Заказ оформлен» и клик по ней
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.BUTTON_WATCH_STATUS)

        # проверка наличия текста «Отменить заказ» на кнопке
        assert BaseMethod.find_element_by_xpath(self, OrderPageLocator.BUTTON_ORDER_CANCEL).text == OrderPageData.CANCEL_ORDER_TEXT