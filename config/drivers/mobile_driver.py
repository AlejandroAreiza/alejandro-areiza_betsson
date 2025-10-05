from config.drivers import ABC, List, WebDriver, WebElement, abstractmethod
from config.dto import Direction


class MobileDriver(ABC):

    @abstractmethod
    def create_mobile_driver(self, config) -> None:
        pass

    @property
    @abstractmethod
    def driver(self) -> WebDriver:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def find_element(self, locator) -> WebElement:
        pass

    @abstractmethod
    def find_elements(self, locator) -> List[WebElement]:
        pass

    @abstractmethod
    def is_element_visible(self, locator) -> bool:
        pass

    @abstractmethod
    def click(self, locator) -> None:
        pass

    @abstractmethod
    def type_text(self, locator, text: str) -> None:
        pass

    @abstractmethod
    def get_text(self, locator) -> str:
        pass

    @abstractmethod
    def swipe(self, locator, direction: Direction) -> None:
        pass
