import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumSmokeTest(unittest.TestCase):

    def setUp(self):
        options: FirefoxOptions = FirefoxOptions()
        options.headless = True
        self.browser: WebDriver = Firefox(options=options)
        self.addCleanup(self.browser.quit)

    def test_can_run_firefox_and_quit(self):
        pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')