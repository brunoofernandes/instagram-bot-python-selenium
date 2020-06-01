from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome('../chromedriver')
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        self.browser.get('https://www.instagram.com/nonapijamas')
        time.sleep(5)
        continue_link = self.browser.find_element_by_partial_link_text('following')
        continue_link.click()
        content = self.browser.find_elements_by_class_name('FPmhX notranslate _0imsa')

        self.browser.execute_script('window.alert("test")')
         

bot = InstagramBot('nonapijamas', '1221212')
bot.signIn()        

     
    
