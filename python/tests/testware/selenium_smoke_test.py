import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumSmokeTest(unittest.TestCase):

    def setUp(self):
        self.browser: WebDriver = Firefox()
        self.addCleanup(self.browser.quit)

    def test_can_run_firefox_and_quit(self):
        pass