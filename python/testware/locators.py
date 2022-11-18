from selenium.webdriver.common.by import By

class StartPageLocators:

    MENU_PANEL = (By.CLASS_NAME, "menu-panel")
    RESOURCE_PANEL = (By.CLASS_NAME, "resource-panel")
    CANVAS = (By.ID, "canvas")
    SAVE_GAME_BUTTON = (By.CSS_SELECTOR, "div#saveGameButton")
    LOAD_GAME_BUTTON = (By.ID, "loadGameButton")
    LOG = (By.ID, "log")
    