
import allure

import locators.order_page_locators as locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, data):
        self.click_on_element(locators.OrderPageLocators.METRO_FIELD)
        metro_locator = (
            locators.OrderPageLocators.METRO[0],
            locators.OrderPageLocators.METRO[1].format(data[3])
        )
        self.find_element(metro_locator)
        self.click_on_element(metro_locator)


    @allure.step('Заполнить данные получателя')
    def fill_customer_form(self, data):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.CUSTOMER_FORM_HEADER)
        self.fill_input_field(locators.OrderPageLocators.NAME_FIELD, data[0])
        self.fill_input_field(locators.OrderPageLocators.SURNAME_FIELD, data[1])
        self.fill_input_field(locators.OrderPageLocators.ADDRESS_FIELD, data[2])
        self.select_metro_station(data)
        self.fill_input_field(locators.OrderPageLocators.PHONE, data[4])

    @allure.step('Тап на кнопку "Далее"')
    def tap_next_step_button(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.NEXT_STEP_BUTTON)
        self.click_on_element(locators.OrderPageLocators.NEXT_STEP_BUTTON)

    @allure.step('Заполнить форму заказа')
    def fill_order_form(self, data):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.ORDER_FORM_HEADER)
        self.click_on_element(locators.OrderPageLocators.DATE_FIELD)
        self.fill_input_field(locators.OrderPageLocators.DATE_FIELD, data[5])
        self.click_on_element(locators.OrderPageLocators.PERIOD_FIELD) # клик на поле срок аренды
        self.click_on_element(locators.OrderPageLocators.ONE_DAY_PERIOD)  # клик на сутки
        self.click_on_element(locators.OrderPageLocators.BLACK_PEARL)  # клик на черный жемчуг

    @allure.step('Тап на кнопку "Заказать" на странице заказа')
    def tap_on_final_order_button(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.SEND_ORDER_BUTTON)
        self.click_on_element(locators.OrderPageLocators.SEND_ORDER_BUTTON)

    @allure.step('Тап на кнопку "Да" в подтверждающей форме заказа')
    def tap_on_confirmation_button(self):
        self.wait_for_visibility_of_element(locators.OrderPageLocators.YES_BUTTON)
        self.click_on_element(locators.OrderPageLocators.YES_BUTTON)


    @allure.step('Тап на Скутер в лого')
    def tap_on_scooter_in_logo(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.LOGO_SCOOTER)
        self.click_on_element(locators.OrderPageLocators.LOGO_SCOOTER)
    @allure.step('Тап на "Посмотреть статус" в подтверждающем информене заказа')
    def tap_on_check_status_button(self):
        self.wait_for_element_to_be_clickable(locators.OrderPageLocators.CHECK_CONFIRM_STATUS_BUTTON)
        self.click_on_element(locators.OrderPageLocators.CHECK_CONFIRM_STATUS_BUTTON)