import allure
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from data.base_page_data import BasePageData
from locators.base_page_locators import BasePageLocator


# Проверка вопросов о важном на главной странице
class TestImportantQuestions:
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
        'question_xpath, answer_xpath, answer_text', [
            [
                BasePageLocator.FIRST_QUESTION,
                BasePageLocator.FIRST_ANSWER,
                BasePageData.FIRST_ANSWER_TEXT,
            ],
            [
                BasePageLocator.SECOND_QUESTION,
                BasePageLocator.SECOND_ANSWER,
                BasePageData.SECOND_ANSWER_TEXT,

            ],
            [
                BasePageLocator.THIRD_QUESTION,
                BasePageLocator.THIRD_ANSWER,
                BasePageData.THIRD_ANSWER_TEXT
            ],
            [
                BasePageLocator.FOURTH_QUESTION,
                BasePageLocator.FOURTH_ANSWER,
                BasePageData.FOURTH_ANSWER_TEXT
            ],
            [
                BasePageLocator.FIFTH_QUESTION,
                BasePageLocator.FIFTH_ANSWER,
                BasePageData.FIFTH_ANSWER_TEXT
            ],
            [
                BasePageLocator.SIXTH_QUESTION,
                BasePageLocator.SIXTH_ANSWER,
                BasePageData.SIXTH_ANSWER_TEXT
            ],
            [
                BasePageLocator.SEVENTH_QUESTION,
                BasePageLocator.SEVENTH_ANSWER,
                BasePageData.SEVENTH_ANSWER_TEXT
            ],
            [
                BasePageLocator.EIGHTH_QUESTION,
                BasePageLocator.EIGHTH_ANSWER,
                BasePageData.EIGHTH_ANSWER_TEXT
            ]
        ],
        ids = [
            "First Question Test Case",
            "Second Question Test Case",
            "Third Question Test Case",
            "Fourth Question Test Case",
            "Fifth Question Test Case",
            "Sixth Question Test Case",
            "Seventh Question Test Case",
            "Eighth Question Test Case"
        ]
    )

    @allure.title('Проверка ответа при клике на вопрос')
    def test_important_questions(self, question_xpath, answer_xpath, answer_text):

        # создание объекта
        base_page = BasePage(self.driver)

        # вызов метода нахождения вопроса на странице и клик по нему
        base_page.click_question(question_xpath)

        # проверка ответа на вопрос
        base_page.check_answer_text(answer_xpath, answer_text)

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()


# Проверка переходов на главной странице
class TestPassage:
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


    @allure.title('Переход со страницы заказа на главную страницу')
    def test_passage_to_scooter(self):

        # создание объекта
        base_page = BasePage(self.driver)

        # поиск логотипа «Самокат» и клик по нему
        base_page.click_scooter_logo()

        # проверка URL-адреса на соответствие
        base_page.check_url(BasePageData.BASE_URL)

    @allure.title('Переход с главной страницы на главную страницу Дзена')
    def test_passage_to_dzen(self):

        # создание объекта
        base_page = BasePage(self.driver)

        # поиск логотипа «Яндекс» и клик по нему
        base_page.click_yandex_logo()

        # переключаемся на новую вкладку
        base_page.switch_to_new_tab()

        # явное ожидание для загрузки новой страницы dzen
        base_page.wait_for_loading_url_by_timeout(BasePageData.DZEN_URL, 10)

        # проверка URL-адреса на соответствие
        base_page.check_url(BasePageData.DZEN_URL)

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()