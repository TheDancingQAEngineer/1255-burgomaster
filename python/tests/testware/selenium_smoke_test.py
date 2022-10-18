import unittest

from python.testware.seleniumwrapper import SeleniumBaseTest


class SeleniumSmokeTest(SeleniumBaseTest):

    def setUp(self):
        options: FirefoxOptions = FirefoxOptions()
        if "GITHUB_ACTIONS" in environ:
            options.headless = True
        self.browser: WebDriver = Firefox(options=options)
        self.addCleanup(self.browser.quit)

    def test_can_run_firefox_and_quit(self):
        self.assertEqual("firefox", self.browser.name)


if __name__ == '__main__':
    unittest.main()