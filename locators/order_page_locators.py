from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопки 'Заказать' на главной странице
    ORDER_BUTTON_1 = (By.XPATH, './/div[starts-with(@class, "Header")]/button[text()="Заказать"]')
    ORDER_BUTTON_2 = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')


    # Заголовок 'Для кого Самокат' в форме данных получателя
    CUSTOMER_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Для кого самокат"]')

    NEXT_STEP_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button') # ??
    SEND_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')

    # Локаторы формы данных получателя
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO = (By.XPATH, '//div[text()="{}"]')
    # METRO = (By.XPATH, '//input[@placeholder="* Станция метро"] and text()="Динамо"')
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # Локаторы формы заказа
    ORDER_FORM_HEADER = (By.XPATH, '//div[text()="Про аренду" and contains(@class, "Order_Header")]')
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    PERIOD_FIELD = (By.XPATH, '//span[@class="Dropdown-arrow"]')
    ONE_DAY_PERIOD = (By.XPATH, '//div[@class = "Dropdown-menu"]/div[text() ="сутки"]')
    BLACK_PEARL = (By.ID, 'black')

    # Заголовок 'Хотите оформить заказ?' в окне подтверждения
    CONFIRMATION_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader__")]')
    # Заголовок 'Заказ оформлен' в форме подтверждения заказа
    CONFIRMATION_ORDER_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')

    # Кнопка "Посмотреть статус" в форме подтвержденного заказа
    CHECK_CONFIRM_STATUS_BUTTON = (By.XPATH, './/button[text()="Посмотреть статус"]')
    # Логотип Самокат
    LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
