from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
      
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        
        if self._user_repository.find_by_username(username) != None:
            raise UserInputError(f"User with username {username} exists already")
        
        if not re.match('^[a-z]+$', username, flags=0):
            raise UserInputError(f"Username needs to contain only letters a-z")
            
        if len(username) < 3:
            raise UserInputError(f"Username is too short")

        if len(password) < 8:
            raise UserInputError(f"Username is too short")
            
        if not re.match('^[A-Za-z0-9]*$', password, flags=0):
            raise UserInputError("Password needs to contain numbers")

        