from pages.base_page import BaseMethod

class ImportantQuestionsPage:

    def __init__(self, driver):
        self.driver = driver


    def click_question(self, question_xpath):
        # ожидание загрузки элемента страницы
        BaseMethod.wait_for_element_by_xpath_by_timeout(self, question_xpath, 10)

        # скролл до элемента страницы
        BaseMethod.scroll_to_element_by_xpath(self, question_xpath)

        # нахождение элемента страницы и клик по нему
        BaseMethod.click_element_by_xpath(self, question_xpath)

    def check_answer_text(self, answer_xpath, answer_text):
        # проверка ответа на вопрос
        assert BaseMethod.find_element_by_xpath(self, answer_xpath).text == answer_text
