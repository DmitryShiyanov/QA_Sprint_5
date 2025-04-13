from selenium.webdriver.common.by import By


class MainLocators:
    # Кнопка поля имя при регистрации
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    # Кнопка поля почта/логин при регистрации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    # Кнопка поля пароль при регистрации
    PASSWORD_FIELD = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']"
    # Кнопка регистрация
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Зарегистрироваться']"
    # Кнопка Войти на странице входа
    LOGIN_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Войти']"
    # Кнопка-ссылка на регистрацию
    REGISTRATION_HREF = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Зарегистрироваться']"
    # Кнопка войти через ссылку регистрации
    REGISTRATION_LOGIN_BUTTON = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Войти']"
    # Кнопка войти в аккаунт на главной странице
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"
    # Текст Вход над страницей входа
    ENTER_TEXT = By.XPATH, "//h2[contains(text(), 'Вход')]"
    # текст ошибки при вводе некорректного пароля
    ERROR_TEXT = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
    # кнопка Оформить заказ
    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"
    # Кнопка на личный кабинет
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"
    # Кнопка "профиль" в личном кабинете
    PROFILE_BUTTON = By.XPATH, "//a[contains(@class, 'Account_link') and text()='Профиль']"
    # Кнопка восстановления пароля
    PASSWORD_RECOVERY_BTN = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']"
    # Кнопка выход на странице личного кабинета
    EXIT_BUTTON = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive') and text()='Выход']"
    # Заголовок на главной странице "Соберите бургер"
    BURGER_TEXT = By.XPATH, "//h1[text()='Соберите бургер']"
    # Кнопка линк на Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    # Логотип Stellar Burgers
    STELLAR_BURGERS_BTN = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"
    # Кнопка булки
    BUN_BUTTON = By.XPATH, "//span[text()='Булки']/parent::div"
    # Кнопка соусы
    SAUCES_BUTTON = By.XPATH, "//span[text()='Соусы']/parent::div"
    # Кнопка начинки
    FILLINGS_BUTTON = By.XPATH, "//span[text()='Начинки']/parent::div"
    # Начинка мясо молюска
    MEAT_MOLUSKIN = By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']"
    # Соус SpicyX
    SAUCE_SPICYX = By.XPATH, "//p[text()='Соус Spicy-X']"
    # Булка краторная
    BUN_CRATOR = By.XPATH, "//p[text()='Краторная булка N-200i']"
