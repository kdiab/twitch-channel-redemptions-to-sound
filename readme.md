# Local Twitch Channel Redemptions To Play Soundbite Locally
##
# Pre-Requisites
## Install python and pip
### Python installation link - https://www.python.org/downloads/
### Pip installation link - https://pypi.org/project/pip/

##
# Compilation
## Open a terminal and make sure python and pip are installed:
### type python --version, if you get an error then it's not installed properly
### type pip --version, same thing applies here

##
##
## Type the following commands
##  pip install -r requirements.txt
##  pyinstaller.exe main.py --onefile
##
##

## What to do if you want to run this
### 1- head to https://dev.twitch.tv/console
### 2- Register an app with any name
### 3- Make the URL of the app equal to http://localhost:17563 (this is for local authorization)
### 4- Copy the client id to APP_ID in the settings folder
### 5- Copy the client secret to APP_SECRET in the settings folder
### 6- Enter your channel name in the TARGET_CHANNEL or a channel you have sufficient permissions in
### 7- Run the script
##

## How to play sounds as channel point redemptions
### 1- Create a channel reward with any name
### 2- Place any mp3 file in the sounds folder with the exact same name as the reward
### 3- Make sure it's a mp3, if you want to use any other file type then figure it out