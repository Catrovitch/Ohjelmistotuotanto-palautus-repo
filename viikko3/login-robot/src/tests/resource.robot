*** Settings ***
Library  ../AppLibrary.py
Library  ../repositories/user_repository.py
Library  ../services/user_service.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${Username}
    Input  ${Password}
    Run Application
