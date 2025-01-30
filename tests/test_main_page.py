import allure
import pytest
from selenium import webdriver
from data.main_page_data import MainPageData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocator


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
        cls.driver.get(MainPageData.BASE_URL)

    @pytest.mark.parametrize(
        'question_xpath, answer_xpath, answer_text', [
            [
                MainPageLocator.FIRST_QUESTION,
                MainPageLocator.FIRST_ANSWER,
                MainPageData.FIRST_ANSWER_TEXT,
            ],
            [
                MainPageLocator.SECOND_QUESTION,
                MainPageLocator.SECOND_ANSWER,
                MainPageData.SECOND_ANSWER_TEXT,

            ],
            [
                MainPageLocator.THIRD_QUESTION,
                MainPageLocator.THIRD_ANSWER,
                MainPageData.THIRD_ANSWER_TEXT
            ],
            [
                MainPageLocator.FOURTH_QUESTION,
                MainPageLocator.FOURTH_ANSWER,
                MainPageData.FOURTH_ANSWER_TEXT
            ],
            [
                MainPageLocator.FIFTH_QUESTION,
                MainPageLocator.FIFTH_ANSWER,
                MainPageData.FIFTH_ANSWER_TEXT
            ],
            [
                MainPageLocator.SIXTH_QUESTION,
                MainPageLocator.SIXTH_ANSWER,
                MainPageData.SIXTH_ANSWER_TEXT
            ],
            [
                MainPageLocator.SEVENTH_QUESTION,
                MainPageLocator.SEVENTH_ANSWER,
                MainPageData.SEVENTH_ANSWER_TEXT
            ],
            [
                MainPageLocator.EIGHTH_QUESTION,
                MainPageLocator.EIGHTH_ANSWER,
                MainPageData.EIGHTH_ANSWER_TEXT
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
        main_page = MainPage(self.driver)

        # вызов метода нахождения вопроса на странице и клик по нему
        main_page.click_question(question_xpath)

        # проверка ответа на вопрос
        main_page.check_answer_text(answer_xpath, answer_text)

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
        cls.driver.get(MainPageData.BASE_URL)


    @allure.title('Переход со страницы заказа на главную страницу')
    def test_passage_to_scooter(self):

        # создание объекта
        main_page = MainPage(self.driver)

        # поиск логотипа «Самокат» и клик по нему
        main_page.click_scooter_logo()

        # проверка URL-адреса на соответствие
        main_page.check_url(MainPageData.BASE_URL)

    @allure.title('Переход с главной страницы на главную страницу Дзена')
    def test_passage_to_dzen(self):

        # создание объекта
        main_page = MainPage(self.driver)

        # поиск логотипа «Яндекс» и клик по нему
        main_page.click_yandex_logo()

        # переключаемся на новую вкладку
        main_page.switch_to_new_tab()

        # проверка URL-адреса на соответствие
        main_page.check_url(MainPageData.DZEN_URL)

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()