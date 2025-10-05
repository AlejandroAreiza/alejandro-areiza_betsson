from business.screens import MobileDriver
from business.screens.login_screen import LoginScreen
from business.screens.products_screen import ProductsScreen


class SwapLabs:

    def __init__(self, mobile_driver: MobileDriver):
        self.mobile_driver = mobile_driver
        self.login_screen = LoginScreen(mobile_driver)
        self.products_screen = ProductsScreen(mobile_driver)

    def get_current_activity(self) -> str:
        """Get the current activity name."""
        return self.mobile_driver.get_current_activity()
