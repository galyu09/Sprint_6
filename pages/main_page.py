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

    def get_text_from_faq_answers(self, locator):
        expected_text = self.driver.find_element(*locator).text
        return expected_text

    # @allure.step('Проверка открытия текста ответа на выбранный вопрос')
    # def check_answer_text(self, answer, expected_text):
    #     self.wait_for_visibility_of_element(answer)
    #     actually_text = self.get_actually_text(answer)
    #     assert actually_text == expected_text
    # actually_text = self.driver.find_element(*locator).text
    # return actually_text

    # @allure.step('Перейти к форме заказа')
    # def go_to_order_page(self):
    #     self.click_to_element(locators.HEADER_ORDER_BUTTON)
    #
    # @allure.step('Получаем текст ответа по порядковому номеру вопроса')
    # def get_answers_text(self):
    # all_elements = self.find_elements_located(SearchPageLocators.NAVI_BAR)
    # return [x.text for x in all_elements]
    #     locator_question_formatted = self.format_locator(locators.QUESTION, num)
    #     locator_answer_formatted = self.format_locator(locators.ANSWER, num)
    #     self.scroll_to_element(locator_question_formatted)
    #     self.click_to_element(locator_question_formatted)
    #     return self.get_text_from_element(locator_answer_formatted)
    #
    # @allure.step('Открываем форму заказа по кнопке вверху страницы')
    # def open_person_info_form_by_header_button(self):
    #     self.click_to_element(locators.HEADER_ORDER_BUTTON)
    #
    # @allure.step('Открываем форму заказа по кнопке внизу страницы')
    # def open_person_info_form_by_content_button(self):
    #     self.scroll_to_element(locators.CONTENT_ORDER_BUTTON)
    #     self.click_to_element(locators.CONTENT_ORDER_BUTTON)
    #
    # @allure.step('Получаем текст заголовка на главной странице')
    # def get_main_header_text(self):
    #     return self.find_element_with_wait(locators.HOME_PAGE_HEADER).text
