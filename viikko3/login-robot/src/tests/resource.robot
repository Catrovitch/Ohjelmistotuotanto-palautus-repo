*** Settings ***
Library  ../AppLibrary.py
Library  ../repositories/user_repository.py
Library  ../services/user_service.py


*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input Create User Command
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Input  create_user

Input Validate Command
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Input  validate