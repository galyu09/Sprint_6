
from pages.base_page import BasePage
import locators.main_page_locators as locators
import allure
import pytest


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проскроллить страницу до раздела FAQ')
    def faq_scroll(self):
        self.scroll_to_element(locators.MainPageLocators.FAQ_TITLE)

    @allure.step('Тапнуть на вопрос из раздела FAQ')
    def tap_on_faq_question(self, num: int):
        self.wait_for_element_to_be_clickable(num)
        self.click_on_element(num)

    @allure.step('')
    def get_text_from_faq_answers(self, locator):
        expected_text = self.driver.find_element(*locator).text
        return expected_text


    @allure.step('Клик на кнопку «Заказать»')
    def click_order_button(self, button):
        self.scroll_to_element(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Клик на самокат в логотипе')
    def tap_on_scooter_in_logo_main(self):
        self.wait_for_element_to_be_clickable(locators.MainPageLocators.LOGO_SCOOTER)
        self.click_on_element(locators.MainPageLocators.LOGO_SCOOTER)

    @allure.step('Берем текущий адрес')
    def take_current_url(self, driver):
        current_url = driver.current_url
        return current_url

    @allure.step('Переключаемся на Дзен')
    def go_to_dzen_by_ya_logo(self):
        self.click_on_element(locators.MainPageLocators.LOGO_YA)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_visibility_of_element(locators.MainPageLocators.DZEN_NEWS_TITLE)



