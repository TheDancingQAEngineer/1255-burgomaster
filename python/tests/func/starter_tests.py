import unittest
import warnings

from python.testware.pageobjects import StartPageObject
from python.testware.seleniumwrapper import SeleniumBaseTest
from python.testware.timeouts import Timeouts

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class StarterTests(SeleniumBaseTest):

    def test_game_loads(self):
        self.browser.get("http://localhost:6699")
        
        # Wait for menu panel to be visible
        try:
            WebDriverWait(self.browser, Timeouts.SHORT).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "menu-panel")))
        except TimeoutException as e:
            raise AssertionError("Menu panel not visible after timeout.") from e
        
        # Wait for resource panel to be visible
        try:
            WebDriverWait(self.browser, Timeouts.SHORT).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "resource-panel")))
        except TimeoutException as e:
            raise AssertionError("Resource panel not visible after timeout.") from e

        # Wait for canvas to be visible
        try:
            WebDriverWait(self.browser, Timeouts.SHORT).until(
                EC.visibility_of_element_located((By.ID, "canvas")))
        except TimeoutException as e:
            raise AssertionError("Canvas not visible after timeout.") from e

        warnings.warn("This test needs refactoring!")
        
        