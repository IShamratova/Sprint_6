from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class BaseMethod:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def wait_for_element_by_xpath_by_timeout(self, xpath, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    def wait_for_new_tab_by_timeout(self, timeout):
        # явное ожидание появления новой вкладки
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(2)
        )

    def wait_for_loading_url_by_timeout(self, url, timeout):
        # явное ожидание для загрузки страницы
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    def scroll_to_element_by_xpath(self, xpath):
        # найди элемент
        element = self.driver.find_element(By.XPATH, xpath)

        # прокрутка страницу до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(0.1)

    def click_element_by_xpath(self, xpath):
        # поиск элемента и клик по нему
        self.driver.find_element(By.XPATH, xpath).click()

    def set_text_to_field_by_xpath(self, xpath, text):
        # поиск поля и ввод данных
        self.driver.find_element(By.XPATH, xpath).send_keys(text)
