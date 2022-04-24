from seleniumbase import BaseCase


class LoginPage(BaseCase):
    homepage_login_button = "//*[@data-qa-id = 'login']"
    login_signup_button = "//*[(text() = 'Sign up' or . = 'Sign up')]"
    login_email_input = "//input[@type = 'email' and @id = 'email' and @name = 'username']"
    login_password_input = "//*[@id = 'password']"
    login_button = "//button[@id = 'logIn']"
    login_need_help_button = "//*[@class = 'need-help' and (text() = 'Need help?' or . = 'Need help?')]"
    login_with_organization_button = "//*[@id = 'logInWithOrganization' and (text() = 'Log In with an Organization' " \
                                     "or . = 'Log In with an Organization')] "
    login_remember_me = "//*[@class = 'form__label--custom' and (text() = 'Remember me' or . = 'Remember me')]"
    wrong_credentials_text = "/html[@class='js  localstorage opacity rgba video placeholder webgl supports " \
                             "no-touchevents backgroundsize bgsizecover cssanimations csstransforms csstransforms3d " \
                             "csstransitions flexbox']/body[@class='animate-done']/div[@class='super-wrap']/form[" \
                             "@class='login-container']/div[@class='login-error fade-in-expand']/div[" \
                             "@class='login-error-container']/p[1] "
    organization_email_input = "//*[@type = 'email' and @name = 'username']"
    organization_login_button = "//*[@data-qa-id = 'log-in-with-sso' and (text() = 'Log In' or . = 'Log In')]"
    organization_email_pw_login = "//*[@data-qa-id = 'log-in-with-email-and-password']"
    organization_cannot_login = "//*[@class = 'login-error-container-code']"
    needhelp_loginHelp = "//h1[(text() = 'Login Help' or . = 'Login Help')]"
    needhelp_email_input = "//*[@type = 'email' and @id = 'forgot-email']"
    needhelp_send_reset_button = "//*[@id = 'resetBtn']"
