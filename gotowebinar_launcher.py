# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from datetime import datetime

#current system time
current_time = datetime.now().strftime("%H:%M:%S")

user_url = str(input("Enter Webinar url:"))
#time when you webinar to get launched

launch_time = str(input("Enter launch time in HH:MM:SS format only: ")) # launch time in HH:MM:SS format only

launch_time2 = datetime.strptime(launch_time, "%H:%M:%S")
current_time2 = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")

i=0

#To check remaining time to launch

for i in range(1000):

    if current_time2 < launch_time2 :
        launch_time3 = datetime.strptime(launch_time, "%H:%M:%S")
        current_time3 = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
        time_remaining = launch_time3 - current_time3
        # print(time_remaining)
        Hr = int(time_remaining.seconds // 3600)
        Min = int(time_remaining.seconds % 3600 / 60.0)
        Sec = int(time_remaining.seconds % 60.0)
        print("Remaining time is:", Hr, "Hr", Min, "Min", Sec, "Sec")
        time.sleep(1)
        i += 1
        if Hr == Min == Sec == 0:
            break
            print("Launching GoToWebinar")
        else:
            continue


# launch_time = print(input("Enter launch time in HH:MM:SS format only"))
# open Chrome
driver = webdriver.Chrome('C:\EXTRAS\Python-Developer-Course-Codes\Auto Gform\chromedriver.exe')

# Open URL
driver.get(user_url)
# driver.get('https://register.gotowebinar.com/register/2618711656922297868')

time.sleep(1)

# wait for one second, until page gets fully loaded
time.sleep(1)
driver.implicitly_wait(2)

# Enters the given values in test fields
fname = driver.find_element_by_id('registrant.firstName')
fname.send_keys('Your_Name')

lname = driver.find_element_by_id('registrant.lastName')
lname.send_keys('Your_Surname')

email = driver.find_element_by_id('registrant.email')
email.send_keys('youe_mail@sample.com')

# Extra input values in case if there are extra questions (Modify them accordingly)
# custQue1 = driver.find_element_by_id('customQuestion1')
# custQue1.send_keys('98')
#
# custQue0 = driver.find_element_by_id('customQuestion0')
# custQue0.send_keys('O')


# submit the registration form
submit = driver.find_element_by_id('registration.submit.button').click()

driver.implicitly_wait(2)
time.sleep(4)


if "https://applauncher.gotowebinar.com/#join/attendee" in driver.current_url:
    driver.maximize_window()
    pyautogui.moveTo(1071, 220)
    time.sleep(5)
    cursor = pyautogui.leftClick(1071, 220)    # Accepts the request of opening GoToOpener

if "https://register.gotowebinar.com/registrationConfirmation" in driver.current_url:

    join_link = driver.find_element_by_link_text('join the webinar.').click()       # click on join the webinar
    driver.maximize_window()
    driver.switch_to.window(driver.window_handles[1])                               # switches the WebDriver focus to new tab
    if "https://applauncher.gotowebinar.com/#join/attendee" in driver.current_url:
        pyautogui.moveTo(1071, 220)
        time.sleep(5)
        cursor = pyautogui.leftClick(1071, 220)    # Accepts the request of opening GoToOpener
    if "https://applauncher.gotowebinar.com/#notStarted" in driver.current_url:     # Closes everything if webinar is not started
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(1)
        driver.close()
        print("Webinar is ended...")