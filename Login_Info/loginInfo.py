from seleniumbase import BaseCase


class LoginInfo(BaseCase):
    correct_username = "zakerysattler@gmail.com"
    correct_password = "Hudlproject1"
    incorrect_username = "incorrect@gmail.com"
    incorrect_password = "Incorrect"
    incomplete_username = "zakerysattler"

