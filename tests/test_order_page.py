import allure
import pytest

from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from tests.data import OrderForm


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('"Заказать" > Заполнить форму > Получить сообщение об успехе')
    @pytest.mark.parametrize(('order_button, data', [(OrderPageLocators.ORDER_BUTTON_1, OrderForm.type1),
                                                   (OrderPageLocators.ORDER_BUTTON_2, OrderForm.type2)]))
    def test_make_order_positive_scenario(self, driver, order_button, data):
        order_page = OrderPage(driver)
        order_page.tap_order_button(order_button)
        order_page.fill_customer_form(data)
        order_page.tap_next_step_button()
        order_page.fill_order_form()
        order_page.tap_on_final_order_button(self)
        order_page.tap_on_confirmation_button(self)
        assert order_page.check_order_form_send_true(self)