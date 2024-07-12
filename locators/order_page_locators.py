from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопки 'Заказать' на главной странице
    ORDER_BUTTON_1 = (By.XPATH, '//button[contains(@class, "Button_Button__")]')
    ORDER_BUTTON_2 = (By.XPATH, '//button[contains(@class, "Button_Middle__")]')

    # Заголовок 'Для кого Самокат' в форме данных получателя
    CUSTOMER_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Для кого самокат"]')

    NEXT_STEP_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button') # ??

    # Локаторы формы данных получателя
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO = (By.XPATH, '//div[contains(text(),"Динамо"]')
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # Локаторы формы заказа
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    PERIOD_FIELD = (By.XPATH, '//span[@class="Dropdown-arrow"]')
    ONE_DAY_PERIOD = (By.XPATH, '//div[@class = "Dropdown-menu"]/div[text() ="сутки"]')
    BLACK_PEARL = (By.ID, 'black')

    # Заголовок 'Хотите оформить заказ?' в окне подтверждения
    CONFIRMATION_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader__")]') # (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    # Заголовок 'Заказ оформлен' в форме подтверждения заказа
    CONFIRMATION_ORDER_FORM_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]') # (By.XPATH, ".//div[text()='Заказ оформлен']")