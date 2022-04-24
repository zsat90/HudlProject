from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

from Login_Info.loginInfo import LoginInfo
from page_objects.login_page_objects import LoginPage
from page_objects.home_page_objects import HomePage
from selenium.webdriver.common.keys import Keys


class LoginScenarios(LoginInfo, LoginPage, HomePage):

    def enter_key_login(self):
        self.send_keys(self.login_email_input, self.correct_username)

        self.send_keys(self.login_password_input, self.correct_password)

        self.send_keys(self.login_button, Keys.ENTER)

    def enter_correct_info(self):
        self.send_keys(self.login_email_input, self.correct_username)

        self.send_keys(self.login_password_input, self.correct_password)

        self.click(self.login_button)

    def navigate_to_login_page(self):
        # Opens the Url
        self.open("https://www.hudl.com/")

        # Verifies the title of the page.
        self.assert_title("Hudl: We Help Teams and Athletes Win")

        # Clicks login button
        self.click(self.homepage_login_button)

    def test_correct_login(self):
        self.navigate_to_login_page()

        # login using correct email and pw
        self.enter_correct_info()

        # Verify elements that show on home page are visible
        self.assert_element(self.explore_link)

        self.assert_element(self.profile_avatar)

        # Looks for the suggestion element If it is not found it will maximize the window and look again.
        try:
            self.assert_text("Suggestions", self.suggestions_text)

        except ElementNotVisibleException:
            self.maximize_window()
            self.assert_text("Suggestions", self.suggestions_text)

    def test_incorrect_username(self):
        self.navigate_to_login_page()

        # Enter incorrect email and validate
        self.send_keys(self.login_email_input, self.incorrect_username)

        self.send_keys(self.login_password_input, self.correct_password)

        self.click(self.login_button)

        # Validates non recognized email text
        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

        self.clear(self.login_email_input)

        # Enters an incomplete email address
        self.send_keys(self.login_email_input, self.incomplete_username)

        self.click(self.login_button)

        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

    def test_incorrect_password(self):
        self.navigate_to_login_page()

        # Enters incorrect password and verifies it doesn't login
        self.send_keys(self.login_email_input, self.correct_username)

        self.send_keys(self.login_password_input, self.incorrect_password)

        self.click(self.login_button)

        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

    def test_blank_input_fields(self):
        self.navigate_to_login_page()

        # Keeps both the username and pw blank and verifies the correct message appears
        self.click(self.login_button)

        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

        # Fills in username and keeps pw blank verifying the correct message appears
        self.send_keys(self.login_email_input, self.correct_username)

        self.click(self.login_button)

        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

        # clears the username and fills in the password verifying correct message appears
        self.clear(self.login_email_input)

        self.send_keys(self.login_password_input, self.correct_password)

        self.click(self.login_button)

        self.assert_text("We didn't recognize that email and/or password. Need help?", self.wrong_credentials_text)

    def test_remember_me(self):

        self.navigate_to_login_page()

        # checks the remember me box
        self.click(self.login_remember_me)

        self.enter_correct_info()

        # verifies that the login was successful
        self.assert_element(self.profile_avatar)

        # Logs the user out and goes back to the login page
        self.click(self.global_user_dropdown)

        self.click(self.logout_button)

        self.click(self.homepage_login_button)

        # Verifies the email field is filled in
        self.is_text_visible("zakerysattler@gmail.com", self.login_email_input)

        # Double checks email is filled in correctly by entering in correct pw and verifying the login
        self.send_keys(self.login_password_input, self.correct_password)

        self.click(self.login_button)

        self.assert_element(self.profile_avatar)

    def test_enter_key(self):
        self.navigate_to_login_page()

        self.enter_key_login()

        # Verify elements that show on home page are visible
        self.assert_element(self.explore_link)

        self.assert_element(self.profile_avatar)

    def test_organization_login(self):
        self.navigate_to_login_page()

        self.click(self.login_with_organization_button)

        self.send_keys(self.organization_email_input, "za")

        self.click(self.organization_login_button)

    # With only two letters entered it will verify if the login button was clicked. It shouldn't be
    # therefore it will enter in a full email and verify the button click
        try:
            print("hello")
            self.assert_element(self.organization_cannot_login)

        except NoSuchElementException:
            print("tried to click the button")

            self.send_keys(self.organization_email_input, self.correct_username)

            self.click(self.organization_login_button)

            self.assert_element(self.organization_cannot_login)
