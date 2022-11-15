*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Create User  sarumann  Palanthir123
    Input Login Command
    
Register With Already Taken Username And Valid Password
    Input Credentials  saruman  asdasd12312
    Input New Command
    Output Should Contain  User with username saruman exists already

Register With Too Short Username And Valid Password
    Input Credentials  sr  asdasdasdasd12323
    Input New Command
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  sauron  1ring
    Input New Command
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  gimli  andmyaxe
    Input New Command
    Output Should Contain  Password needs to contain numbers


*** Keywords ***
Input New Command And Create User
    Create User  saruman  palanthir123s
    Input New Command
Input New Command
    Input  new