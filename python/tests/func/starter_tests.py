import unittest

from python.testware.seleniumwrapper import SeleniumBaseTest


class StarterTests(SeleniumBaseTest):

    def test_title_matches(self):
        self.browser.get("http://localhost:6699")
        self.assertEqual("1255 Burgomaster", self.browser.title)