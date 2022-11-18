from python.testware.locators import StartPageLocators
from python.testware.timeouts import Timeouts

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import Tuple


class BasePageObject:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def verify_element_is_present(self, locator: Tuple[By, str]):
        try:
            WebDriverWait(self._driver, Timeouts.SHORT).until(
                EC.presence_of_element_located(locator))
        except TimeoutException as e:
            raise AssertionError(f"Element \"{locator[1]}\" not present after timeout.") from e

    def verify_element_is_visible(self, locator: Tuple[By, str]):
        try:
            WebDriverWait(self._driver, Timeouts.SHORT).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            raise AssertionError(f"Element \"{locator[1]}\" not visible after timeout.") from e

    def verify_element_is_clickable_and_click(self, locator: Tuple[By, str]):
        try:
            WebDriverWait(self._driver, Timeouts.SHORT).until(
                EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            raise AssertionError(f"Element \"{locator[1]}\" not clickable after timeout.") from e


class StartPageObject(BasePageObject):
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def verify_menu_panel_is_visible(self):
        try:
            self.verify_element_is_visible(StartPageLocators.MENU_PANEL)
        except AssertionError as e:
            raise AssertionError("Menu panel not visible.") from e

    def verify_resource_panel_is_visible(self):
        try:
            self.verify_element_is_visible(StartPageLocators.RESOURCE_PANEL)
        except AssertionError as e:
            raise AssertionError("Resource panel not visible.") from e

    def verify_canvas_is_visible(self):
        try:
            self.verify_element_is_visible(StartPageLocators.CANVAS)
        except AssertionError as e:
            raise AssertionError("Canvas not visible.") from e

    def verify_save_button_is_present(self):
        try:
            self.verify_element_is_present(StartPageLocators.SAVE_GAME_BUTTON)
        except AssertionError as e:
            raise AssertionError("Save button not present") from e

    def verify_load_button_is_present(self):
        try:
            self.verify_element_is_present(StartPageLocators.LOAD_GAME_BUTTON)
        except AssertionError as e:
            raise AssertionError("Load button not present") from e

    def click_save_button(self):
        try:
            self.verify_element_is_clickable_and_click(StartPageLocators.SAVE_GAME_BUTTON)
        except AssertionError as e:
            raise AssertionError("Can't click Save button.") from e

    def click_load_button(self):
        try:
            self.verify_element_is_clickable_and_click(StartPageLocators.LOAD_GAME_BUTTON)
        except AssertionError as e:
            raise AssertionError("Can't click Load button.") from e