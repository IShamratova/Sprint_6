import allure
import pytest
from selenium import webdriver
from pages.important_questions_page import ImportantQuestionsPage
from data.important_questions_page_data import ImportantQuestionsPageData
from locators.important_questions_page_locators import ImportantQuestionsLocator


class TestImportantQuestionsPage:
    driver = None

    @classmethod
    @allure.description('Открытие браузера Firefox')
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

        # раскрытие окна драйвера
        cls.driver.maximize_window()

        # открытие страницы тестового стенда
        cls.driver.get(ImportantQuestionsPageData.BASE_URL)

    @pytest.mark.parametrize(
        'question_xpath, answer_xpath, answer_text', [
            [
                ImportantQuestionsLocator.FIRST_QUESTION,
                ImportantQuestionsLocator.FIRST_ANSWER,
                ImportantQuestionsPageData.FIRST_ANSWER_TEXT,
            ],
            [
                ImportantQuestionsLocator.SECOND_QUESTION,
                ImportantQuestionsLocator.SECOND_ANSWER,
                ImportantQuestionsPageData.SECOND_ANSWER_TEXT,

            ],
            [
                ImportantQuestionsLocator.THIRD_QUESTION,
                ImportantQuestionsLocator.THIRD_ANSWER,
                ImportantQuestionsPageData.THIRD_ANSWER_TEXT
            ],
            [
                ImportantQuestionsLocator.FOURTH_QUESTION,
                ImportantQuestionsLocator.FOURTH_ANSWER,
                ImportantQuestionsPageData.FOURTH_ANSWER_TEXT
            ],
            [
                ImportantQuestionsLocator.FIFTH_QUESTION,
                ImportantQuestionsLocator.FIFTH_ANSWER,
                ImportantQuestionsPageData.FIFTH_ANSWER_TEXT
            ],
            [
                ImportantQuestionsLocator.SIXTH_QUESTION,
                ImportantQuestionsLocator.SIXTH_ANSWER,
                ImportantQuestionsPageData.SIXTH_ANSWER_TEXT
            ],
            [
                ImportantQuestionsLocator.SEVENTH_QUESTION,
                ImportantQuestionsLocator.SEVENTH_ANSWER,
                ImportantQuestionsPageData.SEVENTH_ANSWER_TEXT
            ],
            [
                ImportantQuestionsLocator.EIGHTH_QUESTION,
                ImportantQuestionsLocator.EIGHTH_ANSWER,
                ImportantQuestionsPageData.EIGHTH_ANSWER_TEXT
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

    @allure.description('Проверка ответа при клике на вопрос')
    def test_important_questions(self, question_xpath, answer_xpath, answer_text):

        # создание объекта
        important_questions_page = ImportantQuestionsPage(self.driver)

        # вызов метода нахождения вопроса на странице и клик по нему
        important_questions_page.click_question(question_xpath)

        # проверка ответа на вопрос
        important_questions_page.check_answer_text(answer_xpath, answer_text)

    @classmethod
    @allure.description('Закрытие браузера Firefox')
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()