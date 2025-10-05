from business.screens import AppiumBy, MobileDriver


class CheckoutScreen:

    FIRST_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    ZIP_CODE_INPUT = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    SCREEN_TITLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="CHECKOUT: INFORMATION"]',
    )

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def fill_checkout_information(self, first_name: str, last_name: str, zip_code: str):
        self.driver.type_text(self.FIRST_NAME_INPUT, first_name)
        self.driver.type_text(self.LAST_NAME_INPUT, last_name)
        self.driver.type_text(self.ZIP_CODE_INPUT, zip_code)
        self.driver.click(self.CONTINUE_BUTTON)
