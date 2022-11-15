*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  saruman  Palanthir123
    Input Login Command
    
Register With Already Taken Username And Valid Password
    Input Credentials  saruman  asdasd
    Output Should Contain  User with username Saruman already exists

Register With Too Short Username And Valid Password
    Input Create User Command  sr  asdasdasdasd12323
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Create User Command  sauron  onering1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Create User Command  Gimli  andmyaxe
    Output Should Contain  Password needs to contain numbers