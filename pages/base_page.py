from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators.main_page_locators as locators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # @allure.step('Перейти на страницу')
    # def go_to_site(self, base_url):
    #     return self.driver.get(base_url)

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


    # @allure.step('Получить урл текущей страницы')
    # def get_current_url(self):
    #     current_url = self.driver.current_url
    #     return current_url



    # @allure.step('Переключиться на другое окно браузера')
    # def switch_to_window(self):
    #     self.driver.switch_to.window(self.driver.window_handles[1])







    # @allure.step('Принять cookie')
    # def accept_cookies(self):
    #     self.click_element(HomePageLocators.accept_cookies_button)
    #
    # def delete_all_cookies(self):
    #     self.driver.delete_all_cookies()

    # @allure.step('Нажать Enter для завершения выбора')
    # def press_enter_button(self, locator: tuple[str, str], timeout: int = 10):
    #     self.find_element(locator, timeout).send_keys(Keys.ENTER)
    #
    # @allure.step('Переключить вкладку по номеру')
    # def switch_to(self, window_number: int = 1):
    #     self.driver.switch_to.window(self.driver.window_handles[window_number])
    #
    # @allure.step('Закрыть вкладку')
    # def close_page(self):
    #     self.driver.close()
    #
    # @allure.step('Дождаться отображения URL страницы')
    # def wait_for_url(self, timeout: int = 10):
    #     WebDriverWait(self.driver, timeout).until_not(ec.url_matches('about:blank'))