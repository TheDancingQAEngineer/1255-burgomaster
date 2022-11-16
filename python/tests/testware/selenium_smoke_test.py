import unittest

from python.testware.seleniumwrapper import SeleniumBaseTest

from os import environ
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumSmokeTest(SeleniumBaseTest):

    def test_can_run_firefox_and_quit(self):
        self.assertEqual("firefox", self.browser.name)

    def test_can_access_local_storage_firefox(self):
        self.browser.get("http://localhost:6699")
        local_storage = self.browser.execute_script("return window.localStorage;")
        self.assertIsInstance(local_storage, dict)
        self.assertIn("areso-lang", local_storage)

    def test_can_add_to_local_storage(self):
        self.browser.get("http://localhost:6699")
        self.browser.execute_script('window.localStorage.setItem("cats", "are cute");')
        local_storage = self.browser.execute_script("return window.localStorage;")
        self.assertIn("cats", local_storage)
        self.assertEqual("are cute", local_storage["cats"])

class SeleniumChromeTest(unittest.TestCase):

    def setUp(self):
        self.options: ChromeOptions = ChromeOptions()
        if "GITHUB_ACTIONS" in environ:
            self.options.headless = True
        # self.options.add_experimental_option("w3c", False)
        self.browser: WebDriver = Chrome(options=self.options)
        self.addCleanup(self.browser.quit)

    def test_can_run_chrome_and_quit(self):
        self.assertEqual("chrome", self.browser.name)

    def test_can_access_chrome_local_storage(self):
        self.browser.get("http://localhost:6699")
        local_storage = self.browser.execute_script("return window.localStorage;")
        self.assertIn("areso-lang", local_storage)


if __name__ == '__main__':
    unittest.main()