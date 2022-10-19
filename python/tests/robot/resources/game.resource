*** Settings ***
Library    SeleniumLibrary
Resource   locators.resource

*** Variables ***
${URL}                  http://localhost:6699
${BROWSER}              firefox
${BROWSER HEADLESS}     headlessfirefox

*** Keywords ***
Open Game Page
    Run Keyword If  %{GITHUB_ACTIONS}  ${BROWSER} =  Set Variable ${BROWSER HEADLESS}
    Open Browser   ${URL}    ${BROWSER}

Verify Screen
    Verify Menu Panel
    Verify Resource Panel
    Verify Canvas

Verify Menu Panel
    Wait Until Element Is Visible    ${MENU PANEL}  ${None}  Menu bar not visible  

Verify Resource Panel
    Wait Until Element Is Visible    ${RESOURCE PANEL}  ${None}  Resource panel not visible

Verify Canvas
    Wait Until Element Is Visible    ${CANVAS}  ${None}  Canvas not visible
    