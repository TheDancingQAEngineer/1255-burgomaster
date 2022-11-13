from python.testware.pageobjects import StartPageObject
from python.testware.seleniumwrapper import SeleniumBaseTest


class LocalLoadSaveTest(SeleniumBaseTest):
    
    def test_can_load_local_game(self):
        # What is the right answer?
        # How do I check if the answer is right?
        
        # GIVEN I have local save game
        # WHEN I launch a game in browser
        page = StartPageObject(self.browser)
        self.browser.get("http://localhost:6699")

        # THEN I should see a Load Game button
        # AND I should NOT see tutorial screen or other modal dialogs
        
        # WHEN I click Load Game button
        
        # THEN I should get a log message "Loaded Successfully"
        # AND My stats should be restored from loaded game
        self.fail("Implement the test!")
    