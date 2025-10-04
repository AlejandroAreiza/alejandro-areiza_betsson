from config.drivers.ios_driver import MobileDriver


class IosMobileDriver(MobileDriver):
    def create_mobile_driver(self, config):
        raise NotImplementedError

    @property
    def driver(self):
        raise NotImplementedError

    def quit(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def get_current_activity(self):
        raise NotImplementedError

    def navigate_to(self, url):
        raise NotImplementedError

    def find_element(self, locator):
        raise NotImplementedError

    def find_elements(self, locator):
        raise NotImplementedError

    def is_element_visible(self, locator):
        raise NotImplementedError

    def click(self, locator):
        raise NotImplementedError

    def type_text(self, locator, text):
        raise NotImplementedError

    def get_text(self, locator):
        raise NotImplementedError

    def wait_until_page_load(self, page_title):
        raise NotImplementedError
