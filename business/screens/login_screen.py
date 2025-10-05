from business.screens import AppiumBy, MobileDriver


class LoginScreen:

    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    SCREEN_NAME = (AppiumBy.ACCESSIBILITY_ID, "test-Login")

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def login(self, username: str, password: str):
        self.driver.type_text(self.USERNAME_INPUT, username)
        self.driver.type_text(self.PASSWORD_INPUT, password)
        self.driver.click(self.LOGIN_BUTTON)
        return self

    def is_login_screen_visible(self) -> bool:
        return self.driver.is_element_visible(self.USERNAME_INPUT)
    
    def is_login_button_visible(self) -> bool:
        return self.driver.is_element_visible(self.LOGIN_BUTTON)
