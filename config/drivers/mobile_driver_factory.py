from config.drivers.android_driver.android_mobile_driver import AndroidMobileDriver
from config.drivers.mobile_driver import MobileDriver
from config.dto.desired_capabilities_dto import DesiredCapabilitiesDto


class MobileDriverFactory:
    @staticmethod
    def create_driver(capabilities: DesiredCapabilitiesDto) -> MobileDriver:
        platform = capabilities.platformName.lower()

        if platform == "android":
            driver = AndroidMobileDriver()
            driver.create_mobile_driver(capabilities)
            return driver
        elif platform == "ios":
            raise NotImplementedError("iOS driver not yet implemented")
        else:
            raise ValueError(f"Unsupported platform: {capabilities.platformName}")
