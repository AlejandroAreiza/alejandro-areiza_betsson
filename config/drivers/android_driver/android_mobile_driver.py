from config.drivers.android_driver import (
    EC,
    DesiredCapabilitiesDto,
    Direction,
    Logger,
    MobileDriver,
    TimeoutException,
    UiAutomator2Options,
    WebDriver,
    WebDriverWait,
    webdriver,
)


class AndroidMobileDriver(MobileDriver):

    def __init__(
        self,
        appium_server_url: str = "http://127.0.0.1:4723",
        timeout: int = 10,
        poll_frequency: float = 0.5,
    ):
        self._mobile_driver: WebDriver = None
        self._appium_server_url = appium_server_url
        self._timeout = timeout
        self._poll_frequency = poll_frequency
        self._wait: WebDriverWait = None
        self.logger = Logger.get_logger(__name__)

    def create_mobile_driver(self, desired_capabilities: DesiredCapabilitiesDto):
        try:
            options = UiAutomator2Options().load_capabilities(
                {
                    "platformName": desired_capabilities.platformName,
                    "appium:automationName": desired_capabilities.automationName,
                    "appium:deviceName": desired_capabilities.deviceName,
                    "appium:app": desired_capabilities.app,
                    "appium:appPackage": desired_capabilities.appPackage,
                    "appium:appActivity": desired_capabilities.appActivity,
                    "appium:noReset": desired_capabilities.noReset,
                    "appium:fullReset": desired_capabilities.fullReset,
                    "appium:newCommandTimeout": desired_capabilities.newCommandTimeout,
                    "appium:autoGrantPermissions": desired_capabilities.autoGrantPermissions,
                }
            )
            self._mobile_driver = webdriver.Remote(
                command_executor=self._appium_server_url, options=options
            )
            self._wait = WebDriverWait(
                self._mobile_driver, self._timeout, poll_frequency=self._poll_frequency
            )
            self.logger.info("Android mobile driver created")

        except Exception as e:
            self.logger.error(f"Failed to create Android driver: {e}", exc_info=True)
            raise RuntimeError(f"Failed to create Android driver: {str(e)}")

    @property
    def driver(self) -> WebDriver:
        return self._mobile_driver

    def quit(self):
        try:
            if self._mobile_driver:
                self._mobile_driver.quit()
                self._mobile_driver = None
                self.logger.info("Driver quit")
        except Exception as e:
            self.logger.error(f"Failed to quit driver: {e}", exc_info=True)
            raise

    def reset(self):
        try:
            if self._mobile_driver:
                app_id = self._mobile_driver.capabilities.get("appPackage")
                self._mobile_driver.terminate_app(app_id)
                self._mobile_driver.activate_app(app_id)
        except Exception as e:
            self.logger.error(f"Failed to reset app: {e}", exc_info=True)
            raise

    def find_element(self, locator):
        try:
            self.element = self._wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element found and visible: {locator}")
            return self.element
        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for element {locator} to be visible", exc_info=True
            )
            raise
        except Exception as e:
            self.logger.error(f"Failed to find element {locator}: {e}", exc_info=True)
            raise

    def find_elements(self, locator):
        try:
            elements = self._mobile_driver.find_elements(*locator)
            self.logger.info(f"Found {len(elements)} elements with locator: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Failed to find elements {locator}: {e}", exc_info=True)
            raise

    def is_element_visible(self, locator):
        try:
            self._wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element {locator} is visible")
            return True
        except TimeoutException:
            self.logger.info(f"Element {locator} is not visible (timeout)")
            return False
        except Exception as e:
            self.logger.info(f"Error checking visibility of element {locator}: {e}")
            return False

    def click(self, locator):
        try:
            element = self._wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {e}", exc_info=True)
            raise

    def type_text(self, locator, text):
        try:
            element = self._wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Typed '{text}' into: {locator}")
        except Exception as e:
            self.logger.error(
                f"Failed to type '{text}' into element {locator}: {e}", exc_info=True
            )
            raise

    def get_text(self, locator):
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Text from element {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(
                f"Failed to get text from element {locator}: {e}", exc_info=True
            )
            raise

    def swipe(self, locator, direction: Direction):
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            self._mobile_driver.execute_script(
                "mobile: swipeGesture",
                {
                    "elementId": element.id,
                    "direction": direction.value,
                    "percent": 0.75,
                },
            )
            self.logger.info(f"Swiped {direction.value} on element: {locator}")
        except Exception as e:
            self.logger.error(
                f"Failed to swipe {direction.value} on element {locator}: {e}",
                exc_info=True,
            )
            raise
