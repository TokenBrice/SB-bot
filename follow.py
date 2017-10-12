import time
import sys
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
import os
from slacker import Slacker

slack = Slacker('token') # Where?
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="chomedriver.exe PATH", chrome_options=options)
wait = WebDriverWait(driver, 10)

# LOGIN WITH TWITTER
def login():
    driver.get("https://statusbrew.com/login")
    time.sleep(3)
    os.environ.get("TW_LOGIN", "")
    twitter_pwd = os.environ.get("TW_PWD", "")
    driver.find_element_by_link_text('Login with Twitter').click()
    time.sleep(5)
    username = driver.find_element_by_id('username_or_email')
    username.send_keys(twitter_login)
    password = driver.find_element_by_id('password')
    password.send_keys(twitter_pwd)
    driver.find_element_by_id('allow').click()

# FOLLOWER BOT
failcount = 0
def followerbot():
	global failcount
	try:
		if failcount > 7:
			ending()
		else:
			wait = WebDriverWait(driver, 10)
			element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'sb-activity-user-action-btn')))
			driver.find_element_by_tag_name("sb-activity-user-action-btn").click()
	except NoSuchElementException:
		print('Followerbot: BIP_BOP NoSuchElementException, retry in 15s. BOP_BIP')
		time.sleep(10)
		failcount +=1
	except ElementNotVisibleException:
		print('Followerbot: BIP_BOP ElementNotVisibleException, retry in 15s. BOP_BIP')
		time.sleep(10)
		failcount +=1
	except UnexpectedAlertPresentException:
		print('Followerbot: BIP_BOP UnexpectedAlertPresentException, retry in 15s. BOP_BIP')
		time.sleep(10)
		failcount +=1
	except StaleElementReferenceException:
		print('Unfollowerbot: BIP_BOP StaleElementReferenceException, retry in 7s. BOP_BIP')
		time.sleep(7)
		failcount +=1
	except TimeoutException:
		print('Unfollowerbot: BIP_BOP Timeout Exception, closing program BOP_BIP')
		time.sleep(7)
		failcount +=1

# UNFOLLOW BUTTON CLICKER LOOP
fcount = 0
def followloop():
	global fcount
	print("\n BIP_BOP Followerbot started BOP_BIP")
	todos = [followerbot] * 200
	for doit in todos:
		doit()
		fcount += 1
		time.sleep(1)
	print(fcount)
	return fcount

# CLOSE + LOG FUNCTION
def ending(fcount):
	print(fcount)
	print("Ending+logging function runned. %d followed" % fcount)
	slack.chat.post_message('#channel', 'TWITTERBOT REPORT: Interactions with %d accounts' % fcount)
	driver.quit()
	sys.exit()

login()
time.sleep(5)

# Command Menu
while True:
	print("""
	1.Follow/Unfollow x 200
	2.Report
	3.Exit
	""")
	ans = input("BIP_BOP What would you like to do? BOP_BIP ")
	if ans == "1":
		followloop()
	if ans == "2":
		report(fcount)
	if ans == "3":
		ending(fcount)
