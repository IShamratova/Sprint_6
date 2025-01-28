import allure
from data.order_page_data import OrderPageData
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator
from locators.order_page_locators import OrderPageLocator


class OrderPage(BasePage):

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_order_button(self):
        # поиск кнопки «Заказать» и клик по ней
        self.click_element_by_xpath(MainPageLocator.NAV_BUTTON_ORDER)

    @allure.step('Ввод персональных данных')
    def set_personal_info(
            self,
            first_name_text,
            last_name_text,
            address_text,
            station_metro_text,
            phone_number
    ):
        # явное ожидание для загрузки страницы
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.HEADER_SCOOTER, 3)

        # поиск поля «Имя» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.FIRST_NAME, first_name_text)

        # поиск поля «Фамилия» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.LAST_NAME, last_name_text)

        # поиск поля «Адрес: куда привезти заказ», клик по нему и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.ADDRESS, address_text)

        # поиск поля «Станция метро» и клик по нему
        self.click_element_by_xpath(OrderPageLocator.METRO)

        # поиск поля «Станция метро» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.METRO, station_metro_text)

        # поиск поля станции метро «Парк культуры» и клик по нему
        self.click_element_by_xpath(OrderPageLocator.STATION_METRO)

        # поиск поля «Телефон: на него позвонит курьер» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.PHONE, phone_number)

        # поиск кнопки «Далее» и клик по ней
        self.click_element_by_xpath(OrderPageLocator.BUTTON_NEXT)

    @allure.step('Ввод данных по заказу')
    def set_order_info(
            self,
            delivery_date,
            comment_courier_text
    ):
        # явное ожидание для загрузки страницы
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.HEADER_RENTAL, 3)

        # Поиск поля «Срок аренды» и клик по нему
        self.click_element_by_xpath(OrderPageLocator.RENTAL_PERIOD)

        # явное ожидание для загрузки выпадающего списка
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.NUMBER_DAYS, 3)

        # поиск поля «трое суток» и клик по нему
        self.click_element_by_xpath(OrderPageLocator.NUMBER_DAYS)

        # поиск поля «Когда привезти самокат» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.WHEN_BRING_SCOOTER, delivery_date)

        # поиск чек-бокса «чёрный жемчуг» и клик по нему
        self.click_element_by_xpath(OrderPageLocator.COLOUR_SCOOTER)

        # поиск поля «Комментарий для курьера» и ввод данных
        self.set_text_to_field_by_xpath(OrderPageLocator.COMMENT_COURIER, comment_courier_text)

        # поиск нижней кнопки «Заказать» и клик по ней
        self.click_element_by_xpath(OrderPageLocator.LOWER_BUTTON_ORDER)

    @allure.step('Проверка заказа')
    def check_order(self):
        # явное ожидание для загрузки всплывающего окна «Хотите оформить заказ?»
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.HEADER_WANT_ORDER, 3)

        # поиск кнопки «Да» окна «Хотите оформить заказ?» и клик по ней
        self.click_element_by_xpath(OrderPageLocator.BUTTON_YES)

        # явное ожидание для загрузки всплывающего окна «Заказ оформлен»
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.HEADER_ORDER_REGISTER, 3)

        # поиск кнопки «Посмотреть статус» окна «Заказ оформлен» и клик по ней
        self.click_element_by_xpath(OrderPageLocator.BUTTON_WATCH_STATUS)

        # явное ожидание для загрузки всплывающего окна «Заказ оформлен»
        self.wait_for_element_by_xpath_by_timeout(OrderPageLocator.BUTTON_ORDER_CANCEL, 3)

        # проверка наличия текста «Отменить заказ» на кнопке
        assert self.find_element_by_xpath(OrderPageLocator.BUTTON_ORDER_CANCEL).text == OrderPageData.CANCEL_ORDER_TEXT