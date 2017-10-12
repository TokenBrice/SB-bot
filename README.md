# StatusBrew-bot

## Purpose
Simple Python script made for learning purposes. Using Selenium and Statusbrew.com, it allows for semi-automated and targeted Twitter follow/defolow activities.
 **It's a learning project, the code if far from perfect.** Some could reasonably argue it's ugly and I would probably agree with them. At least it does the job. Feel free to improve it!

## Setting up your Twitter Credentials and chromedriver path
The script use environement variables to avoid storing credential in plaintext. You'll have to input your credentials in the terminal before running the script. Both scripts require two variables to run:
Twitter Account ID: TW_LOGIN
Twitter Account Password: TW_PWD
#### Windows (Powershell)
$env:TW_LOGIN = 'twitterlogin'
$env:TW_PWD = 'twitterpassword'
#### Bash
export TW_LOGIN='twitterlogin'
export TW_PWD='twitterpassword'

#### Chromedriver path
Edit the script at line 20

## Requirements
* You'll need an account on [StatusBrew](https://www.statusBrew.com) to use the script.
* [Selenium Python library](http://selenium-python.readthedocs.io/) is also required.
* [Slacker](https://github.com/os/slacker) for slack reporting.

## Other options to set up

* [Slack token](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens) - line 17
* Slack channel and message - line 85
* Loop amount (default is 200) - line 74

## Why Selenium?
I have no idea of StatusBrew's devs tolerance for bots. Using Selenium, even though it makes the bot slower also makes it more **human-like** on the other end since everything happens within a browser. I've been using this bot (in even more primitive forms than the current one) for years without hitting restrictions or raising alarms. Moreover, because the bot work on top of StatusBrew, it gave me access to all the powerful targeting/sorting features of the interface without having to build it myself.
