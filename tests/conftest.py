import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()