import allure
from data.main_page_data import MainPageData
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator


class MainPage(BasePage):

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        # поиск кнопки «Заказать» и клик по ней
        self.click_element_by_xpath(MainPageLocator.NAV_BUTTON_ORDER)

        # явное ожидание для загрузки страницы
        self.wait_for_loading_url_by_timeout(MainPageData.BASE_URL + 'order', 3)

        # поиск логотипа «Самокат» и клик по нему
        self.click_element_by_xpath(MainPageLocator.LOGO_SCOOTER)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        # явное ожидание для загрузки страницы
        self.wait_for_element_by_xpath_by_timeout(MainPageLocator.LOGO_SCOOTER, 3)

        # поиск логотипа «Яндекс» и клик по нему
        self.click_element_by_xpath(MainPageLocator.LOGO_YANDEX)

    @allure.step('Нажатие на вопрос')
    def click_question(self, question_xpath):
        # явное ожидание загрузки страницы элемента
        self.wait_for_element_by_xpath_by_timeout(question_xpath, 10)

        # прокрутка страницы до элемента
        self.scroll_to_element_by_xpath(question_xpath)

        # явное ожидание загрузки элемента страницы
        self.wait_for_element_by_xpath_by_timeout(question_xpath, 10)

        # нахождение элемента страницы и клик по нему
        self.click_element_by_xpath(question_xpath)

    @allure.step('Проверка ответа')
    def check_answer_text(self, answer_xpath, answer_text):
        # проверка ответа на вопрос
        assert self.find_element_by_xpath(answer_xpath).text == answer_text