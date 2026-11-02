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

    def login(self, login, password):
        self.field_login(login)
        self.field_password(password)
        self.login_button()


    @pytest.mark.parametrize(
        "login, password, expected",
        [
            ("user1", "password1", "Welcome, user1!"),
            ("anastasia1", "mypassword1", "Wrong login or password"),
            ("anastasia2", "mypassword2", "Wrong login or password"),
            ("", "", "Login and password are required (minimum 3 and 6 characters)"),
            ("user1", "password2", "Wrong login or password"),
            ("user!@#", "password", "Wrong login or password"),
            ("user", "pass!@#", "Wrong login or password"),
            ("us", "password", "Login must be at least 3 characters"),
            ("user", "pas", "Password must be at least 6 characters"),
            ("<script>", "password", "Wrong login or password"),
            ("user", "", "Password is required (minimum 6 characters)"),
            ("", "password", "Login is required (minimum 3 characters)"),
        ],
        ids=[
            "valid_login",
            "invalid_login_1",
            "invalid_login_2",
            "empty_fields",
            "invalid_password",
            "login_with_special_characters",
            "password_with_special_characters",
            "login_too_short",
            "password_too_short",
            "login_html_injection",
            "password_empty",
            "login_empty",
        ],
    )
    def test_login_form(self, login, password, expected):
        self.login(login, password)

        if expected.startswith("Welcome"):
            assert self.welcome_message_text() == expected
        else:
            assert self.error_message_text() == expected