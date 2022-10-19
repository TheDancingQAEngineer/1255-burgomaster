from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from python.testware.locators import StartPageLocators
from python.testware.timeouts import Timeouts


class BasePageObject:
    def __init__(self) -> None:
        pass


class StartPageObject(BasePageObject):
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self._driver = driver

    def verify_menu_panel_is_visible(self):
        try:
            self._wait_for_element_to_be_visible(StartPageLocators.MENU_PANEL)
        except AssertionError as e:
            raise AssertionError("Menu panel not visible") from e

    def verify_resources_panel_is_visible(self):
        raise NotImplementedError

    def verify_canvas_is_visible(self):
        raise NotImplementedError

    def _wait_for_element_to_be_visible(self, locator: tuple[By, str]):
        try:
            element = WebDriverWait(self._driver, Timeouts.SHORT).until(
                EC.visibility_of_element_located(locator)
            )
        finally:
            raise AssertionError(f"Element not visible by locator: {locator[1]}.")

