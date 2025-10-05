import time
from config.drivers.android_driver import (
    EC,
    DesiredCapabilitiesDto,
    Logger,
    MobileDriver,
    TimeoutException,
    UiAutomator2Options,
    WebDriver,
    WebDriverWait,
    webdriver,
)


class AndroidMobileDriver(MobileDriver):
    """Android mobile driver implementation using Appium."""

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
        """Get the mobile driver instance."""
        return self._mobile_driver

    def quit(self):
        """Quit the driver."""
        try:
            if self._mobile_driver:
                self._mobile_driver.quit()
                self._mobile_driver = None
                self.logger.info("Driver quit")
        except Exception as e:
            self.logger.error(f"Failed to quit driver: {e}", exc_info=True)
            raise

    def reset(self):
        """Reset the app to initial state by terminating and reactivating."""
        try:
            if self._mobile_driver:
                app_id = self._mobile_driver.capabilities.get("appPackage")
                self._mobile_driver.terminate_app(app_id)
                self._mobile_driver.activate_app(app_id)
        except Exception as e:
            self.logger.error(f"Failed to reset app: {e}", exc_info=True)
            raise

    def get_current_activity(self) -> str:
        """Get the current activity of the app."""
        try:
            time.sleep(3)
            activity = self._mobile_driver.current_activity
            self.logger.info(f"Current activity: {activity}")
            return activity
        except Exception as e:
            self.logger.error(f"Failed to get current activity: {e}", exc_info=True)
            raise

    def navigate_to(self, url):
        """Navigate to URL."""
        try:
            self._mobile_driver.get(url)
            self.logger.info(f"Navigated to: {url}")
        except Exception as e:
            self.logger.error(f"Failed to navigate to URL {url}: {e}", exc_info=True)
            raise

    def find_element(self, locator):
        """Find element by locator with fluent wait for visibility."""
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element found and visible: {locator}")
            return element
        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for element {locator} to be visible", exc_info=True
            )
            raise
        except Exception as e:
            self.logger.error(f"Failed to find element {locator}: {e}", exc_info=True)
            raise

    def find_elements(self, locator):
        """Find elements by locator."""
        try:
            elements = self._mobile_driver.find_elements(*locator)
            self.logger.info(f"Found {len(elements)} elements with locator: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Failed to find elements {locator}: {e}", exc_info=True)
            raise

    def is_element_visible(self, locator):
        """Check if element is visible."""
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element {locator} is visible")
            return True
        except TimeoutException:
            self.logger.info(f"Element {locator} is not visible (timeout)")
            return False
        except Exception as e:
            self.logger.warning(f"Error checking visibility of element {locator}: {e}")
            return False

    def click(self, locator):
        """Click element with explicit wait for clickable."""
        try:
            element = self._wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {e}", exc_info=True)
            raise

    def type_text(self, locator, text):
        """Type text into element with explicit wait for clickable (editable)."""
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
        """Get text from element with explicit wait for visibility."""
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

    def wait_until_page_load(self, page_title):
        """Wait until page loads."""
        try:
            self.logger.info(f"Waiting for page to load: {page_title}")
            # Implementation depends on how you want to verify page load
            # This is a placeholder
            self.logger.info(f"Page loaded: {page_title}")
        except Exception as e:
            self.logger.error(
                f"Failed waiting for page {page_title}: {e}", exc_info=True
            )
            raise
