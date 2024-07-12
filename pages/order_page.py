import allure

import locators.order_page_locators as locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Тап на кнопку "Заказать" на главной')
    def tap_order_button(self, order_button):
        self.find_element(order_button)
        self.click_on_element(order_button)

    @allure.step('Заполнить данные получателя')
    def fill_customer_form(self, data):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.CUSTOMER_FORM_HEADER)
        self.fill_input_field(locators.OrderPageLocators.NAME_FIELD, data)
        self.fill_input_field(locators.OrderPageLocators.SURNAME_FIELD, data)
        self.fill_input_field(locators.OrderPageLocators.ADDRESS_FIELD, data)
        self.click_on_element(locators.OrderPageLocators.METRO_FIELD)
        self.scroll_to_element(locators.OrderPageLocators.METRO)
        self.click_on_element(locators.OrderPageLocators.METRO)
        self.fill_input_field(locators.OrderPageLocators.PHONE, data)

    @allure.step('Тап на кнопку "Далее"')
    def tap_next_step_button(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.NEXT_STEP_BUTTON)
        self.click_on_element(locators.OrderPageLocators.NEXT_STEP_BUTTON)

    @allure.step('Заполнить форму заказа')
    def fill_order_form(self, data):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.ORDER_FORM_HEADER)
        self.click_on_element(locators.OrderPageLocators.DATE_FIELD)
        self.fill_input_field(locators.OrderPageLocators.DATE_FIELD, data)
        self.click_on_element(locators.OrderPageLocators.PERIOD_FIELD) # клик на поле срок аренды
        self.click_on_element(locators.OrderPageLocators.ONE_DAY_PERIOD)  # клик на сутки
        self.click_on_element(locators.OrderPageLocators.BLACK_PEARL)  # клик на черный жемчуг

    @allure.step('Тап на кнопку "Заказать" на странице заказа')
    def tap_on_final_order_button(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.SEND_ORDER_BUTTON)
        self.click_on_element(locators.OrderPageLocators.BLACK_PEARL)
    @allure.step('Тап на кнопку "Да" в подтверждающей форме заказа')
    def tap_on_confirmation_button(self):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.CONFIRMATION_FORM_HEADER)
        self.click_on_element(locators.OrderPageLocators.CONFIRMATION_FORM_HEADER)
    @allure.step('Проверка наличия формы подтверждения оформленного заказа')
    def check_order_form_send_true(self):
        self.driver.find_element(locators.OrderPageLocators.CONFIRMATION_ORDER_FORM_HEADER).is_displayed()