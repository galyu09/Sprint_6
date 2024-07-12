import allure
import pytest

from pages.main_page import MainPage
from tests import data
from locators.main_page_locators import MainPageLocators
from tests.data import ImportantQuestions


@allure.suite('Тесты главной страницы')
class TestMainPage:

    @allure.title('Проверка блока «Вопросы о важном»')
    @allure.description('Проверка соответствия текста ответов пунктам выпадающего списка')
    @pytest.mark.parametrize(
        'num, answer, expected_text',
        [
            (MainPageLocators.NUM_1, MainPageLocators.ANS_1, ImportantQuestions.text_1),
            (MainPageLocators.NUM_2, MainPageLocators.ANS_2, ImportantQuestions.text_2),
            (MainPageLocators.NUM_3, MainPageLocators.ANS_3, ImportantQuestions.text_3),
            (MainPageLocators.NUM_4, MainPageLocators.ANS_4, ImportantQuestions.text_4),
            (MainPageLocators.NUM_5, MainPageLocators.ANS_5, ImportantQuestions.text_5),
            (MainPageLocators.NUM_6, MainPageLocators.ANS_6, ImportantQuestions.text_6),
            (MainPageLocators.NUM_7, MainPageLocators.ANS_7, ImportantQuestions.text_7),
            (MainPageLocators.NUM_8, MainPageLocators.ANS_8, ImportantQuestions.text_8)
        ]
    )
    def test_tap_on_faq_returns_expected_text(self, driver, num, answer, expected_text):
        main_page = MainPage(driver)
        main_page.faq_scroll()
        main_page.wait_for_visibility_of_element(num)
        main_page.tap_on_faq_question(num)
        main_page.wait_for_visibility_of_element(answer)
        assert main_page.get_text_from_faq_answers(answer) == expected_text



    # def test_click_to_faq_returns_true_answers(self, driver, num, expected_text):
    #     main_page = MainPage(driver)
    #     main_page.tap_num_question_button()
    #     assert main_page.get_text_on_element(num) == expected_text
    #     # main_page.accept_cookies()
    #     # assert main_page.get_expected_text(num) == expected_text