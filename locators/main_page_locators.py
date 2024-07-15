from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка 'Заказать' вверху на главной
    UPPER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')

    # Вторая кнопка 'Заказать' после карты статусов на главной
    LOWER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')


    # Заголовок блока "Вопросы о важном"
    FAQ_TITLE = (By.XPATH, ".//div[text()='Вопросы о важном']")

    # Вопросы раздела "Вопросы о важном":
    NUM_1 = (By.XPATH, "//div[@id='accordion__heading-0']/parent::div")
    NUM_2 = (By.XPATH, "//div[@id='accordion__heading-1']/parent::div")
    NUM_3 = (By.XPATH, "//div[@id='accordion__heading-2']/parent::div")
    NUM_4 = (By.XPATH, "//div[@id='accordion__heading-3']/parent::div")
    NUM_5 = (By.XPATH, "//div[@id='accordion__heading-4']/parent::div")
    NUM_6 = (By.XPATH, "//div[@id='accordion__heading-5']/parent::div")
    NUM_7 = (By.XPATH, "//div[@id='accordion__heading-6']/parent::div")
    NUM_8 = (By.XPATH, "//div[@id='accordion__heading-7']/parent::div")

    # Ответы раздела "Вопросы о важном":
    ANS_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    ANS_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    ANS_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    ANS_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    ANS_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    ANS_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    ANS_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    ANS_8 = (By.XPATH, "//div[@id='accordion__panel-7']")


    # Логотип Самокат
    LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    # Логотип Яндекс
    LOGO_YA = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')
    DZEN_NEWS_TITLE = (By.XPATH, '//div[@data-testid="floor-title-text" and text()="Новости"]')
