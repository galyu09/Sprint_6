
import allure
import pytest
from pages.main_page import MainPage


class TestTransitionPage:

    @allure.description('Проверка перехода на главную по клику на самокат в логотипе')
    def test_go_to_main_from_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.tap_on_scooter_in_logo_main()
        assert main_page.take_current_url(driver) == 'https://qa-scooter.praktikum-services.ru/'


    @allure.description('Проверка перехода на Дзен по тапу на логотип Яндекс')
    def test_go_to_zen_from_ya_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_dzen_by_ya_logo()
        assert main_page.take_current_url(driver) == 'https://dzen.ru/?yredirect=true'

