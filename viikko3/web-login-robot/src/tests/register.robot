
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page


*** Test Cases ***
Register With Valid Username And Password
    Go To Main Page
    Click Link  Register new user 
    Set Username  Sauron
    Set Password  theonering123
    Set Password Confirmation  theonering123
    Click Button  Register

Register With Too Short Username And Valid Password
    Go To Main Page
    Click Link  Register new user 
    Set Username  Sa
    Set Password  theonering123
    Set Password Confirmation  theonering123
    Click Button  Register

Register With Valid Username And Too Short Password
    Go To Main Page
    Click Link  Register new user 
    Set Username  Sauron
    Set Password  t3
    Set Password Confirmation  theonering123
    Click Button  Register

Register With Nonmatching Password And Password Confirmation
    Go To Main Page
    Click Link  Register new user 
    Set Username  Sauron
    Set Password  theonering123
    Set Password Confirmation  theonering1234
    Click Button  Register

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
