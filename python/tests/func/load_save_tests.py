from python.testware.locators import StartPageLocators
from python.testware.pageobjects import StartPageObject
from python.testware.seleniumwrapper import SeleniumBaseTest
from python.testware.timeouts import Timeouts

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocalLoadSaveTest(SeleniumBaseTest):
    
    def test_can_load_local_game(self):
        # What is the right answer?
        # How do I check if the answer is right?
        
        # GIVEN I have local save game
        # WHEN I launch a game in browser
        page = StartPageObject(self.browser)
        self.browser.get("http://localhost:6699")
        # AND I add a mock 'game' to Local Storage
        mock_game = {
            "gold": 55,
            "pop": 42,
            "gems": 20
        }

        self.browser.execute_script(f'window.localStorage.setItem("game", "{mock_game}");')
        # And I refresh browser
        self.browser.refresh()

        # THEN I should be able to get 'game' object from local storage 
        game = self.browser.execute_script('return window.localStorage.getItem("game");')
        self.assertIsNotNone(game)
        # AND I should see a Load Game button
        page.verify_load_button_is_present()
        # AND I should NOT see tutorial screen or other modal dialogs
        
        # WHEN I click Load Game button
        page.click_load_button()
        
        # THEN I should get a log message "Loaded Successfully"
        successful_load_message = "игра загружена успешно"
        try:
            WebDriverWait(self.browser, Timeouts.SHORT).until(
                EC.text_to_be_present_in_element(StartPageLocators.LOG, successful_load_message)
            )
        except TimeoutException as e:
            raise AssertionError(f"Message \'{successful_load_message}\' not in log after timeout.") from e

        # AND My stats should be restored from loaded game
        self.fail("Implement the test!")
    