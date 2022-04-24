from seleniumbase import BaseCase


class HomePage(BaseCase):
    explore_link = "//*[@href = '/explore' and (text() = 'Explore' or . = 'Explore')]"
    profile_avatar = "//*[@class = 'hui-globaluseritem__avatar' and (text() = 'ZS' or . = 'ZS')]"
    hamburger_menu = "//*[@class = 'hui-secondarynav__open-menu']"
    suggestions_text = "//span[(text() = 'Suggestions' or . = 'Suggestions')]"
    global_user_dropdown = "(.//*[normalize-space(text()) and normalize-space(.)='ZS'])[1]/following::div[1]"

    logout_button = "//div[@id='ssr-webnav']/div/div/nav/div[4]/div[2]/div[2]/div[3]/a"
