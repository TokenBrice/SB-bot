# StatusBrew-bot

## PURPOSE
Simple Python script made for learning purposes. Using Selenium and Statusbrew.com, it allows for semi-automated and targeted Twitter follow/defolow activities.
 **It's a learning project, the code if far from perfect.** Some could reasonably argue it's ugly and I would probably agree with them. At least it does the job. Feel free to improve it!

## CREDENTIALS
All the variables you need to edit are marked with the following syntax: {{YOUR_TWITTER_ACCOUNT}}

## FILES
- Follow.py is a semi-automated bot: it lets you define the targeting manually.
- Unfollow.py can be fully automated using TaskScheduler or CRON jobs. Make sure to change your `CleanUp Suggestion` URL

## REQUIREMENTS
* You'll need an account on [StatusBrew](https://statusbrew.com/bberdah) to use the script.
* [Selenium Python library](http://selenium-python.readthedocs.io/) is also required.
* [Slacker](https://github.com/os/slacker) for slack reporting.

## WHY SELENIUM
I have no idea of StatusBrew's devs tolerance for bots. Using Selenium, even though it makes the bot slower also makes it more **human-like** on the other end since everything happens within a browser. I've been using this bot (in even more primitive forms than the current one) for years without hitting restrictions or raising alarms. Moreover, because the bot work on top of StatusBrew, it gave me access to all the powerful targeting/sorting features of the interface without having to build it myself.
