import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocator
from locators.order_page_locators import OrderPageLocator


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента по XPATH')
    def find_element_by_xpath(self, xpath):
        # поиск и выдача элемента
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Ожидание появления элемента по XPATH с заданным таймаутом')
    def wait_for_element_by_xpath_by_timeout(self, xpath, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step('Ожидание загрузки новой вкладки с заданным таймаутом')
    def wait_for_new_tab_by_timeout(self, timeout):
        # явное ожидание появления новой вкладки
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(2)
        )

    @allure.step('Ожидание загрузки ресурса с заданным таймаутом')
    def wait_for_loading_url_by_timeout(self, url, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Прокрутка страницы до элемента по XPATH')
    def scroll_to_element_by_xpath(self, xpath):
        # поиск элемента
        element = self.driver.find_element(By.XPATH, xpath)

        # прокрутка страницы до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажатие на элемент по XPATH')
    def click_element_by_xpath(self, xpath):
        # поиск элемента и клик по нему
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step('Ввод текста в поле по XPATH')
    def set_text_to_field_by_xpath(self, xpath, text):
        # поиск поля и ввод данных
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        # поиск кнопки «Заказать» и клик по ней
        BasePage.click_element_by_xpath(self, BasePageLocator.NAV_BUTTON_ORDER)

        # явное ожидание для загрузки страницы
        BasePage.wait_for_element_by_xpath_by_timeout(self, OrderPageLocator.HEADER_SCOOTER, 3)

        # поиск логотипа «Самокат» и клик по нему
        BasePage.click_element_by_xpath(self, BasePageLocator.LOGO_SCOOTER)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        # явное ожидание для загрузки страницы
        BasePage.wait_for_element_by_xpath_by_timeout(self, BasePageLocator.LOGO_SCOOTER, 3)

        # поиск логотипа «Яндекс» и клик по нему
        BasePage.click_element_by_xpath(self, BasePageLocator.LOGO_YANDEX)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        # явное ожидание для загрузки новой вкладки
        BasePage.wait_for_new_tab_by_timeout(self, 10)

        # получение списка всех вкладок
        windows = self.driver.window_handles

        # переключение на новую вкладку
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def check_url(self, url):
        assert self.driver.current_url == url

    @allure.step('Нажатие на вопрос')
    def click_question(self, question_xpath):
        # явное ожидание загрузки страницы элемента
        BasePage.wait_for_element_by_xpath_by_timeout(self, question_xpath, 10)

        # прокрутка страницы до элемента
        BasePage.scroll_to_element_by_xpath(self, question_xpath)

        # явное ожидание загрузки элемента страницы
        BasePage.wait_for_element_by_xpath_by_timeout(self, question_xpath, 10)

        # нахождение элемента страницы и клик по нему
        BasePage.click_element_by_xpath(self, question_xpath)

    @allure.step('Проверка ответа')
    def check_answer_text(self, answer_xpath, answer_text):
        # проверка ответа на вопрос
        assert BasePage.find_element_by_xpath(self, answer_xpath).text == answer_text