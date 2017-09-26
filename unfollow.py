import time
import sys
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Script is ready to use once you set up
# Basic function: Chromdriverpath (line 17), Twitter login and password as environment variables (see readme)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="CHROMDRIVER.EXE PATH", chrome_options=options)

# LOGIN WITH TWITTER
def login():
	driver.get("https://statusbrew.com/")
	time.sleep(3)
	twitter_login = os.environ.get("TW_LOGIN", "")
	twitter_pwd = os.environ.get("TW_PWD", "")
	driver.find_element_by_link_text('Log in').click()
	time.sleep(1)
	driver.find_element_by_link_text('Log in with Twitter').click()
	time.sleep(5)
	username = driver.find_element_by_id('username_or_email')
	username.send_keys(twitter_login)
	password = driver.find_element_by_id('password')
	password.send_keys(twitter_pwd)
	driver.find_element_by_id('allow').click()

# UNFOLLOW-BUTTON CLICKER + FAIL COUNTER
failcount = 0
def unfollowerbot():
    global failcount
    try:
        if failcount>15:
            ending()
        else:
            driver.find_element_by_xpath('//*[@id="infinite-container"]/div/div[1]/div[1]/md-card/md-card-title/md-card-title-text/div/md-card-actions/div/com-activity-user-action-btn/button').click()
    except NoSuchElementException:
        print('Unfollowerbot: BIP_BOP NoSuchElementException, retry in 7s. BOP_BIP')
        time.sleep(7)
        failcount +=1
    except ElementNotVisibleException:
        print('Unfollowerbot: BIP_BOP ElementNotVisibleException, retry in 7s. BOP_BIP')
        time.sleep(7)
        failcount +=1
    except StaleElementReferenceException:
        print('Unfollowerbot: BIP_BOP StaleElementReferenceException, retry in 7s. BOP_BIP')
        time.sleep(7)
        failcount +=1

# UNFOLLOW BUTTON CLICKER LOOP
ufcount = 0
def unfollowloop():
    global ufcount
    print("\n BIP_BOP Unfollowerbot started BOP_BIP")
    todos = [unfollowerbot] * 2000
    for doit in todos:
        doit()
        ufcount += 1
        time.sleep(0.1)
    return ufcount
            
# CLOSE + LOG FUNCTION
def ending():
        print("Ending+logging function runned %d unfollowed" % ufcount)
        driver.quit()
        sys.exit()

# FETCH UNFOLLOW PAGE AND RUN
login()
time.sleep(5)
driver.get("https://app.statusbrew.com/p/audience/twitter/102725697/activity/nfb?exclude_rf_days=7")
# URL of the page listing all the account you follow. The filter "exclude_rf_days" let you exclude recently followed people.
time.sleep(5)
unfollowloop()
