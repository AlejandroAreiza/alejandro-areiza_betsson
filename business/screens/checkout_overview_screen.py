from business.screens import AppiumBy, Direction, List, MobileDriver, WebElement


class CheckoutOverviewScreen:

    SCREEN_TITLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="CHECKOUT: OVERVIEW"]',
    )
    FINISH_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("test-FINISH"))',
    )
    ITEM_TOTAL = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Item total:"))',
    )
    TAX = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Tax:"))',
    )
    TOTAL = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Total:"))',
    )
    ORDER_LIST = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("test-Item"))',
    )

    CONFIRMATION_POPUP = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("THANK YOU FOR YOU ORDER")',
    )

    INCOMPLETE_POPUP = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: INCOMPLETE!")

    BACKHOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-BACK HOME")
    PRODUCT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("test-Item")',
    )
    DELETE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-Delete")

    def __init__(self, driver: MobileDriver):
        self.driver = driver

    def is_checkout_overview_screen_visible(self) -> bool:
        return self.driver.is_element_visible(self.SCREEN_TITLE)

    def is_order_list_visible(self) -> bool:
        return self.driver.is_element_visible(self.ORDER_LIST)

    def is_order_summary_visible(self) -> bool:
        return (
            self.driver.is_element_visible(self.ITEM_TOTAL)
            and self.driver.is_element_visible(self.TAX)
            and self.driver.is_element_visible(self.TOTAL)
        )

    def tap_finish(self):
        self.driver.click(self.FINISH_BUTTON)

    def is_confirmation_popup_visible(self) -> bool:
        return self.driver.is_element_visible(self.CONFIRMATION_POPUP)

    def is_incomplete_order_popup_visible(self) -> bool:
        return self.driver.is_element_visible(self.INCOMPLETE_POPUP)

    def get_confirmation_text(self) -> str:
        return self.driver.get_text(self.CONFIRMATION_POPUP)

    def remove_all_products(self):
        while True:
            elements: List[WebElement] = self.driver.find_elements(self.ORDER_LIST)
            if not elements:
                break
            self.driver.swipe(self.PRODUCT, Direction.LEFT)
            self.driver.click(self.DELETE_BUTTON)
