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

    def get_screen_title(self) -> str:
        """Get the login screen title text."""
        return self.driver.get_text(self.SCREEN_NAME)

    def is_login_screen_visible(self) -> bool:
        """Check if login screen is visible."""
        return self.driver.is_element_visible(self.USERNAME_INPUT)
