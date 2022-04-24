from page_objects.login_page_objects import LoginPage


class ValidateLogin(LoginPage):

    def navigate_to_login_page(self):
        # Opens the Url
        self.open("https://www.hudl.com/")

        # Verifies the title of the page.
        self.assert_title("Hudl: We Help Teams and Athletes Win")

        # Clicks login button
        self.click(self.homepage_login_button)

    def test_validate_login_page(self):
        # Opens the Url
        self.open("https://www.hudl.com/")

        # Verifies the title of the page.
        self.assert_title("Hudl: We Help Teams and Athletes Win")

        # Verify Login button and click
        self.click(self.homepage_login_button)

        # Verify login url
        login_url = self.get_current_url()
        self.assert_true("login" in login_url)

        # Verify elements on the login page
        self.assert_element(self.login_signup_button)

        self.assert_element(self.login_email_input)

        self.assert_element(self.login_password_input)

        self.assert_element(self.login_button)

        self.assert_element(self.login_need_help_button)

        self.assert_element(self.login_remember_me)

        self.assert_element(self.login_with_organization_button)

    def test_validate_organization_login(self):
        self.navigate_to_login_page()

        # Verifies Login with Organization
        self.click(self.login_with_organization_button)

        self.assert_element(self.organization_email_input)

        self.send_keys(self.organization_email_input, "test")

        self.assert_element(self.organization_login_button)

        self.assert_element(self.organization_email_pw_login)

        self.click(self.organization_email_pw_login)

    def test_validate_needhelp_login(self):
        self.navigate_to_login_page()

        # Verifies the need help button
        self.click(self.login_need_help_button)

        self.assert_text("Login Help", self.needhelp_loginHelp)

        self.assert_element(self.needhelp_email_input)

        self.assert_element(self.needhelp_send_reset_button)
