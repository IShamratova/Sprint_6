import allure
from selenium import webdriver
from pages.base_page import BaseMethod
from data.passage_data import PassageData
from locators.order_page_locators import OrderPageLocator


class TestPassagePage:
    driver = None

    @classmethod
    @allure.description('Открытие браузера Firefox')
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

        # раскрытие окна драйвера
        cls.driver.maximize_window()

        # открытие страницы тестового стенда
        cls.driver.get(PassageData.BASE_URL)

    @allure.description('Переход со страницы заказа на главную страницу')
    def test_passage_to_scooter(self):
        # поиск кнопки «Заказать» и клик по ней
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.HIGH_BUTTON_ORDER)

        # явное ожидание для загрузки страницы
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_SCOOTER, 3)

        # поиск логотипа «Самокат» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.LINK_SCOOTER)

        # проверка URL-адреса на соответствие логина
        assert self.driver.current_url == PassageData.BASE_URL

    @allure.description('Переход с главной страницы на главную страницу Дзена')
    def test_passage_to_dzen(self):
        # явное ожидание для загрузки страницы
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.LINK_SCOOTER, 3)

        # сохраняем handle текущей вкладки
        original_window = self.driver.current_window_handle

        # поиск логотипа «Яндекс» и клик по нему
        BaseMethod.click_element_by_xpath(self, OrderPageLocator.LINK_DZEN)

        # явное ожидание для загрузки новой страницы dzen
        BaseMethod.wait_for_new_tab_by_timeout(self, 10)

        # получаем список всех вкладок
        windows = self.driver.window_handles

        # переключаемся на новую вкладку
        for window in windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        # явное ожидание для загрузки новой страницы dzen
        BaseMethod.wait_for_loading_url_by_timeout(self, PassageData.DZEN_URL, 10)

        # проверка URL-адреса на соответствие dzen
        assert self.driver.current_url == PassageData.DZEN_URL

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()