# StatusBrew-bot

## Purpose
Simple Python scripts made for learning purposes. Using Selenium and Statusbrew.com, they allow for semi-automated and targeted Twitter follow/defolow activities.
 **It's a learning project, the code if far from perfect.** Some could reasonably argue it's ugly and I would probably agree with them. At least it does the job. Feel free to improve it!

## Disclaimer
* **The defollow (unfollow.py) script is fully autonomous** and can be ran with TaskScheduler/CRON jobs.
* **The follow (follow.py) script still requires manual intervention**, as I wanted to keep control over the targeted accounts for follower scraping.

## Setting up your Twitter Credentials
The script use environement variables to avoid storing credential in plaintext. You'll have to input your credentials in the terminal before running the script. Both scripts require two variables to run:
Twitter Account ID: TW_LOGIN
Twitter Account Password: TW_PWD
#### Windows (Powershell)
$env:TW_LOGIN = 'twitterlogin'
$env:TW_PWD = 'twitterpassword'
#### Bash
export TW_LOGIN='twitterlogin'
export TW_PWD='twitterpassword'

## Requirements
* You'll need an account on [StatusBrew](https://www.statusBrew.com) to use the script.
* [Selenium Python library](http://selenium-python.readthedocs.io/) is also required.
* [CALLR Python SDK](https://www.callr.com/docs/) is optional, if you want automated SMS reporting.

## Why Selenium?
I have no idea of StatusBrew's devs tolerance for bots. Using Selenium, even though it makes the bot slower also makes it more **human-like** on the other end since everything happens within a browser. I've been using this bot (in even more primitive forms than the current one) for years without hitting restrictions or raising alarms. Moreover, because the bot work on top of StatusBrew, it gave me access to all the powerful targeting/sorting features of the interface without having to build it myself.
