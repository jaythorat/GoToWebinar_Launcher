# GoToWebinar Launcher : 
## Now you'll never be late for your Webinars or Meetings on the GoToWebinar Platform

## About

Are you popular for always being late for meetings? Yeah me too..
 
So this script is the solution just enter all your details in it and it will connect you to meeting automatically even if you forgot to..Now onwards no more #LateComer tags :p

I got to know about the module named selenium and pyautogui and I decided to make a script/code which will automatically launch webinar/meeting at the given time

## Working

This is how the script works:

1. When you run the code it calculates the remaining time and executes the commands on provided time.
2. It will launch the browser, fill up your details and it'll register you for the webinar.
3. And the software in your pc "GoToOpener" will be launched automatically


Now I can go to sleep, eat, or scroll peacefully! ;)

## Dependencies

This project uses following dependencies in Python (install using `pip`):

* `selenium`
* `WebDriver`
* `pyautogui`

Compatible with: Any PC or laptop with Python and Selenium installed on Chrome, Safari, Opera, and Edge. _(Just modify the code accordingly)_

## Installation

1. Install `Python` (Any 3.x.x version)
2. Install `selenium` (https://pypi.org/project/selenium/)
3. Install `Webdriver` (For Chrome: https://chromedriver.chromium.org/, similarly find a specific driver for your browser)
4. Install `pyautogui` (https://pypi.org/project/PyAutoGUI/)
### OR
    pip install -r requirements.txt
	

## Usage

1. Make sure you have the dependencies installed and have followed the steps mentioned in _Installation_ section above.
2. Make sure you have entered the correct information of your webdriver in the code.
3. Replace all the existing links and data according to your need.
4. Execute: `gotowebinar_launcher.py`

## Precautions

1. Make sure `launch_time` input is in `HH:MM:SS` format.
2. This Code is optimized for `1980*1080` screens if your screen size is diff please change the values on 
   lines 81,83,91,93 or contact me at `j.thorat10@gmail.com`
3. Make sure `GoToOpener` is already installed on your pc.
4. You can change the `driver.implicitly_wait()` & `time.sleep()` values according to your network and system speed.
