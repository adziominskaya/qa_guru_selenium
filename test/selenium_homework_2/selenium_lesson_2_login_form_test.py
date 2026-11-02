import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginForm:
    URL = "https://qa-guru.github.io/one-page-form/login.html"

    LOGIN_FIELD = (By.ID, "login-input")
    PASSWORD_FIELD = (By.ID, "password-input")
    LOGIN_BUTTON = (By.ID, "submit-button")
    LOGOUT_BUTTON = (By.ID, "logout-button")
    WELCOME_MESSAGE = (By.ID, "welcome-message")
    ERROR_MESSAGE = (By.ID, "error-message")

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        yield
        self.driver.quit()

    def field_login(self, login):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(login)

    def field_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def welcome_message_text(self):
        self.wait.until(ec.visibility_of_element_located(self.WELCOME_MESSAGE))
        return self.driver.find_element(*self.WELCOME_MESSAGE).text

    def error_message_text(self):
        self.wait.until(ec.visibility_of_element_located(self.ERROR_MESSAGE))
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    @pytest.mark.parametrize("login, password, expected", [
        ("user1", "password1", f"Welcome, user1!")
    ])
    def test_valid_data_login(self, login, password, expected):
        self.field_login(login)
        self.field_password(password)
        self.login_button()
        assert self.welcome_message_text() == expected

    @pytest.mark.parametrize("login, password, expected", [
        ("anastasia1", "mypassword1", "Wrong login or password"),
        ("anastasia2", "mypassword2", "Wrong login or password"),
    ])
    def test_invalid_login(self, login, password, expected):
        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == expected

    def test_empty_fields(self):
        self.login_button()
        assert self.error_message_text() == "Login and password are required (minimum 3 and 6 characters)"

    def test_invalid_password(self):
        login = "user1"
        password = "password2"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Wrong login or password"


    def test_login_with_special_characters(self):
        login = "user!@#"
        password = "password"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Wrong login or password"


    def test_password_with_special_characters(self):
        login = "user"
        password = "pass!@#"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Wrong login or password"


    def test_login_too_short(self):
        login = "us"
        password = "password"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Login must be at least 3 characters"


    def test_password_too_short(self):
        login = "user"
        password = "pas"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Password must be at least 6 characters"


    def test_login_html_injection(self):
        login = "<script>"
        password = "password"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Wrong login or password"

    def test_password_empty(self):
        login = "user"
        password = ""

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Password is required (minimum 6 characters)"


    def test_login_empty(self):
        login = ""
        password = "password"

        self.field_login(login)
        self.field_password(password)
        self.login_button()

        assert self.error_message_text() == "Login is required (minimum 3 characters)"