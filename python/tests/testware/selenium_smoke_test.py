import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumSmokeTest(unittest.TestCase):

    def test_can_run_firefox_and_quit(self):
        browser: WebDriver = Firefox()
        browser.quit()