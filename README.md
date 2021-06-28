# Currently being revised! 

Twitter bot tutorial: Jumpstart Program 2021 edition

Let's make a bot!! These instructions were written for participants in the [2021 Jumpstart Program](https://www.lib.ncsu.edu/jumpstart), but they're publicly viewable for anyone to follow.

**Required libraries:** tweepy 3.5, requests, time, os, random. Written in Python 3. 

---

## Installation Specifications

For this workshop, you will need to:
1. Install [Visual Studio Code](https://code.visualstudio.com/) (VS Code)
1. Install [Anaconda](https://www.anaconda.com/products/individual) (which will install Python for you and some of the required libraries listed above)
1. Install the [Tweepy library](http://docs.tweepy.org/en/latest/install.html)
1. Create a new [Twitter](https://twitter.com) account, and use that account to apply for [developer status](https://developer.twitter.com/en/apply-for-access). (Don't use an existing Twitter account that has followers, as you're about to send a zillion tweets that your followers might not want to clutter their feed.) It may take a few hours (occasionally longer) for a developer account to be approved.

## Fork this repository
Get this code onto your local machine. 

1. Fork this repository by clicking the button labeled 'fork' in the top right corner of this window. This will add this repository to your own GitHub account. 

2. Clone the repository to your local machine.
- Go to the repository in your account: github.com/(your account name)/bot-tutorial-jumpstart-2021
- Select the green "Code" button and copy the URL there, which should end in .git
- In your terminal [mac] or command line [windows], navigate to the folder where you  want this repository to live (your Desktop, for example), and then run the following command to clone the repository to that location: `git clone [repository url ending in .git]`

3. Navigate into that repository with the command `cd bot-tutorial-jumpstart-2021`

## Running Code in VS Code: test.py (optional)

To test things out and get familiar with how we will be running code for this workshop, follow these steps:

1. Using your finder or search box, find the folder on your desktop. Open the folder and open the file test.py in Visual Studio Code.
2. To run the code, click the green triangle in the upper right corner of the VS Code window. 
3. Look for “Hello, there!” printed in the Terminal part of this window (the lower half). 

[View an annotated screenshot of how to edit and run Python code in VS Code](http://robincamille.com/ncsu/vscode_screenshot_python.png)

## Get credentials from your Twitter account 
Give your Twitter script the passwords it needs to send tweets via code instead of using the Twitter website. (These steps may have changed since they were written, as Twitter is continually updating their developer account process.)

1. Go to https://developer.twitter.com/en/portal/apps/new and name your new app. (If you get an  error message when you click the "Complete" button, try going to the old [sign-up form](https://developer.twitter.com/en/apps/create) instead)
 - This name isn't public; call it something like JumpstartBot
 
1. On the app's `Settings` page, scroll down to App Permissions and edit it, changing it from "Read only" to "Read & Write"

1. Find the app's `Keys and Tokens` page (the tab next to the app's Settings)
 - (Re)generate "Consumer API key & secret" and "Access token & secret"

2. Copy Consumer API Key/Secret and Access Token/Secret to **credentials.template** 

3. Save that file as a new file named **credentials.py**
- (Why save with a new filename? Later on, you'll commit and push the changes you make to these files using Git, and those changes will be publicly viewable on your GitHub account. But you don't want to share your bot account's credentials/passwords. The file called .gitignore has credentials.py listed as a file to ignore, so Git will never even see it, and it won't get sent to your GitHub account.)

## Basic bot: listbot.py

This script is a basic Twitter bot. It will tweet three things from a **list** inside the script.

1. Go to the bot-tutorial-jumpstart-2021 folder. Click on `listbot.py` to see the code

2. Take a look at the script and try to figure out what it's doing. Use the comments (preceded by #) for context.

3. Clicking the green "run" triangle will run the bot. A Terminal will appear at the bottom of the screen with the output

*Change it up!*
- In `tweet_list`, add new things for your bot to tweet
- Increase/decrease time between tweets in `time.sleep(15)` (15 is the number of seconds) 

## Intermediate bot: textbot.py

This script sends out five tweets from the first five lines of an external .txt file, `phrases_coined_by_shakespeare.txt`

1. Go to the bot-tutorial-jumpstart-2021 folder. Click on `textbot.py`

2. Also look at `phrases_coined_by_shakespeare.txt` to see the text

3. Take a look at both files and try to figure out what it's doing. Use the comments (preceded by #) for context.

4. Select `Run`

*Change it up!*
- Make the bot send more or fewer tweets, or change which lines, by editing the numbers in `for line in tweettext[0:5]`. 
   - `[0:5]` means from the first thing up to (but not including) the #5 thing. Programming languages consider 0 to be the first number, so what we'd call "line one" is actually "line zero" to the computer, and "line six" to humans is "line five" to the computer.
 - Make a new .txt file for the bot to tweet from. For example, pick a book or poem from gutenberg.org. Then, in textbot.py, replace `phrases_coined_by_shakespeare.txt` with the `newfilename.txt`
 
## Advanced bot: talk-mashup-bot.py

This script mixes up talk titles from ALA Annual Conferences 2016–2021.  First, it takes a list of talks and splits those titles into potential beginnings and endings. Then, it chooses a random beginning and a random ending, smushes them together into a new talk title, and tweets it. This script also introduces a function, `splitTitle()`, and demonstrates how to choose a random item in a list using Python's `random` library.

*Change it up!*
- In the tweet (`tweet_text` on line ~89), add a bit of text that comes before the new talk title, like "Your new ALA session is..."
- Add a new "splitting point" to the list `split_at`, like the word "with."
- Use another .txt file instead of `ala_all-talk-titles.txt`. For example, make a new .txt file with movie names or book titles. 
- Advanced: Some parts of this code are repetitive. Use a `for` loop in the part of the script that makes `beginners_list_final` and `enders_list_final` so that lines of code don't repeat.


## Commit your changes with Git 

You've made changes to these scripts since you first forked them. Now you'll practice *committing* and *pushing* those changes so you have a record of your versions.

1. In the Terminal window of VS Code, type `git status` and hit the return (enter) key to see the files you've changed.
1. Then type `git add listbot.py` (or another filename) and hit return
1. (Optional) Type `git status` and hit return again to check what that did
1. Type `git commit -m "Changed what the bot tweets"` (or another way to describe your change) and hit return

[View an annotated screenshot of how to use Git in VS Code](http://robincamille.com/ncsu/vscode_screenshot_git.png)

### Push your changes with Git 

At some point, you'll want the changes you've committed on your machine to appear on your GitHub repository. 

1. In the Terminal window again, type `git push origin master` and hit the return key. You should see a message of success.


---

This tutorial and its updated materials were originally put together by Robin Davis (@robincamille) and Mark Eaton (github.com/MarkEEaton) for a pre-conference workshop at [Code4Lib 2018](http://2018.code4lib.org/).

*See original repo: https://github.com/robincamille/bot-tutorial*

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy* (Blueprints section).  April 2016. (Verbose write-up featuring [code from a previous version](https://github.com/robincamille/bot-tutorial) of this workshop.)
