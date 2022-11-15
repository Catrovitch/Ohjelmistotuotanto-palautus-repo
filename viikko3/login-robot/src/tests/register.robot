*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Register With Valid Username And Password
    Create User  saruman  Palanthir123
    Input Login Command
    
Register With Already Taken Username And Valid Password
    Input Credentials  saruman  asdasd
    Input New Command
    Output Should Contain  User with username Saruman already exists

Register With Too Short Username And Valid Password
    Input Credentials  sr  asdasdasdasd12323
    Input New Command
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  sauron  onering1
    Input New Command
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Gimli  andmyaxe
    Input New Command
    Output Should Contain  Password needs to contain numbers


*** Keywords ***
Reset Database
    Reset