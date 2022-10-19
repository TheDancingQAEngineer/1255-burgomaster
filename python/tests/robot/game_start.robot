*** Settings ***
Resource    resources/game.resource

*** Variables ***
${BLANK URL}      http://localhost:6699
${BROWSER}        Firefox

*** Test Cases ***
Game Loads
    Open Game Page
    Verify Screen
    Close Browser