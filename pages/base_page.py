from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Найти элемент')
    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Дождаться загрузки элемента')
    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Дождаться, когда элемент станет кликабельным')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Проскроллить до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Заполнить поле значением')
    def fill_input_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

