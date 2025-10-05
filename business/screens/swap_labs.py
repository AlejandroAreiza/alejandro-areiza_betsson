from business.screens import MobileDriver
from business.screens.cart_screen import CartScreen
from business.screens.checkout_overview_screen import CheckoutOverviewScreen
from business.screens.checkout_screen import CheckoutScreen
from business.screens.login_screen import LoginScreen
from business.screens.products_screen import ProductsScreen


class SwapLabs:

    def __init__(self, mobile_driver: MobileDriver):
        self.mobile_driver = mobile_driver
        self.login_screen = LoginScreen(mobile_driver)
        self.products_screen = ProductsScreen(mobile_driver)
        self.cart_screen = CartScreen(mobile_driver)
        self.checkout_screen = CheckoutScreen(mobile_driver)
        self.checkout_overview_screen = CheckoutOverviewScreen(mobile_driver)
