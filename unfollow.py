# SYSTEM IMPORT
import time
import sys
import os
from random import randint

# SELENIUM + REQUIRED EXCEPTIONS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from slacker import Slacker

# WEBDRIVER OPTIONS

slack = Slacker('{{YOUR_SLACK_TOKEN}}')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="{{YOUR_CHROMEDRIVER_PATH}}", chrome_options=options)
wait = WebDriverWait(driver, 10)

# LOGIN WITH TWITTER
def login():
    driver.get("https://statusbrew.com/login")
    time.sleep(3)
    driver.find_element_by_link_text('Login with Twitter').click()
    time.sleep(5)
    username = driver.find_element_by_id('username_or_email')
    username.send_keys('{{YOUR_TWITTER_ACCOUNT}}')
    password = driver.find_element_by_id('password')
    password.send_keys('{{YOUR_TWITTER_PASSWORD}}')
    driver.find_element_by_id('allow').click()

# FOLLOWER BOT
failcount = 0
def followerbot():
	global failcount
	global fcount
	try:
		if failcount > 5:
			ending(fcount)
		elif fcount % 100 == 0:
			slack.chat.post_message('#twitter-bot-report', 'TwitterBot reporting for @Gwapitapp - 100 people unfollowed')
		else:
			wait = WebDriverWait(driver, 10)
			element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'sb-activity-user-action-btn')))
			driver.find_element_by_tag_name("sb-activity-user-action-btn").click()
		
	except NoSuchElementException:
		print('Followerbot: BIP_BOP NoSuchElementException, retry in 7s. BOP_BIP')
		time.sleep(7)
		failcount +=1
	except ElementNotVisibleException:
		print('Followerbot: BIP_BOP ElementNotVisibleException, retry in 7s. BOP_BIP')
		time.sleep(7)
		failcount +=1
	except UnexpectedAlertPresentException:
		print('Followerbot: BIP_BOP UnexpectedAlertPresentException, retry in 7s. BOP_BIP')
		time.sleep(7)
		failcount +=1
	except StaleElementReferenceException:
		print('Unfollowerbot: BIP_BOP StaleElementReferenceException, retry in 5s. BOP_BIP')
		time.sleep(5)
		failcount +=1
	except TimeoutException:
		print('Unfollowerbot: BIP_BOP Timeout Exception, closing program BOP_BIP')
		time.sleep(5)
		failcount +=1

# UNFOLLOW BUTTON CLICKER LOOP
fcount = 1
def followloop():
	global fcount
	print("\n BIP_BOP Followerbot started BOP_BIP")
	todos = [followerbot] * 310
	for doit in todos:
		doit()
		fcount += 1
		time.sleep(randint(1,5))
	print(fcount)
	return fcount

# CLOSE/END FUNCTION
def ending(fcount):
	print(fcount)
	driver.quit()
	sys.exit()

login()
time.sleep(5)

# UNFOLLOW

driver.get("{{YOUR_STATUSBREW_ACCOUNT_URL}}/cleanup_suggestions")
time.sleep(10)
followloop()
