import json
import unittest

from python.testware.seleniumwrapper import SeleniumBaseTest

from os import environ
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.command import Command


class SeleniumSmokeTest(SeleniumBaseTest):

    def test_can_run_firefox_and_quit(self):
        self.assertEqual("firefox", self.browser.name)

    def test_can_access_local_storage_firefox(self):
        self.browser.get("http://localhost:6699")
        local_storage = self.browser.execute_script("return window.localStorage;")
        self.assertIn("areso-lang", local_storage)


class SeleniumChromeTest(unittest.TestCase):

    def setUp(self):
        self.options: ChromeOptions = ChromeOptions()
        if "GITHUB_ACTIONS" in environ:
            self.options.headless = True
        self.options.add_experimental_option("w3c", False)
        self.browser: WebDriver = Chrome(options=self.options)
        self.addCleanup(self.browser.quit)

    def test_can_run_chrome_and_quit(self):
        self.assertEqual("chrome", self.browser.name)

    def test_can_access_chrome_local_storage(self):
        self.browser.get("http://localhost:6699")
        storage_keys = self.browser.execute(Command.GET_LOCAL_STORAGE_KEYS)
        self.assertIn("value", storage_keys.keys())
        self.assertIn("areso-lang", storage_keys["value"])


if __name__ == '__main__':
    unittest.main()