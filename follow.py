import time
import datetime
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Optional CALLR API used for SMS reporting
# import callr
# api = callr.Api("CALLRLogin","CALLRpwd")

# Script is ready to use once you set up
# Basic function: Chromdrivepath (line 23), SB login (34), SB password (36)
# Optional SMS Reporting: CALLR logins (15), Destination number (82)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="CHROMDRIVER.EXE PATH", chrome_options=options)

# CALLR LOGIN WITH TWITTER
def login():
		driver.get("https://statusbrew.com/")
		time.sleep(3)
		driver.find_element_by_link_text('Log in').click()
		time.sleep(1)
		driver.find_element_by_link_text('Log in with Twitter').click()
		time.sleep(5)
		username = driver.find_element_by_id('username_or_email')
		username.send_keys('YOURLOGIN')
		password = driver.find_element_by_id('password')
		password.send_keys('YOURPASSWORD')
		driver.find_element_by_id('allow').click()

# FOLLOWER BOT
failcount = 0
def followerbot():
	global failcount
	try:
		if failcount > 7:
			ending()
		else:
			driver.find_element_by_xpath('//*[@id="infinite-container"]/div/div[1]/div[5]/md-card/md-card-title/md-card-title-text/div/md-card-actions/div/com-activity-user-action-btn/button').click()
			time.sleep(1)
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

# UNFOLLOW BUTTON CLICKER LOOP
fcount = 0
def followloop():
	global fcount
	print("\n BIP_BOP Followerbot started BOP_BIP")
	todos = [followerbot] * 500
	for doit in todos:
		doit()
		fcount += 1
	print(fcount)
	return fcount

# CLOSE + LOG FUNCTION
def ending(fcount):
	print(fcount)
	print("Ending+logging function runned. %d followed" % fcount)
	# OPTIONAL SMS REPORT api.call('sms.send', 'SMS', '+336XXXXXXXX', 'Followbot done, %d followed' % fcount, None)
	driver.quit()
	sys.exit()

login()
time.sleep(5)

# Command Menu
while True:
	print("""
	1.Follow
	2. Exit
	""")
	ans = input("BIP_BOP What would you like to do? BOP_BIP ")
	if ans == "1":
		followloop()
	if ans == "2":
		ending(fcount)
