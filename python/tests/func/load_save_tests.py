from python.testware.pageobjects import StartPageObject
from python.testware.seleniumwrapper import SeleniumBaseTest


class LocalLoadSaveTest(SeleniumBaseTest):
    
    def test_can_save_game(self):
        page = StartPageObject(self.browser)
        self.browser.get("http://localhost:6699")
        # Verify we're on game page
        # Locate save game button and click
        page.verify_save_button_is_present()
        page.click_save_button()
        # Should see log message "Save game successful"
        self.fail("Implement the test!")
    