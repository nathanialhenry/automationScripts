# This script signs in to CoreForm and copies the last hours entered and submits them
# Best if used in conjunction with task scheduler or cron job

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import argparse

# Add arguments for the script
parser = argparse.ArgumentParser(description="Enter necessary fields to run the Time Script(--driver for ChromeDriver Path, --user for Username, --password for Password ")
parser.add_argument("--driver", type = str, default = 'D:\\timeScript\\chromedriver_win32\\chromedriver.exe', help = "chromedriver path")
parser.add_argument("--url", type = str, help= "Coreform URL")
parser.add_argument("--user", type=str, help="CoreForm Username")
parser.add_argument("--password", type=str, help="CoreForm Password")
args = parser.parse_args()

# initialize driver, and accesses the CoreForm webpage, added an implicit wait for slow loads
driver = webdriver.Chrome(args.driver)
driver.implicitly_wait(10)
driver.get(args.url)

# Enters Username/Password and Submits
username = driver.find_element_by_id("username")
username.send_keys(args.user)

password = driver.find_element_by_id("password")
password.send_keys(args.password)

submit = driver.find_element_by_id("login")
submit.click()

# copies the last entry
copyButton = driver.find_element_by_class_name('icon_button.glyphicon.glyphicon-hand-down')
copyButton.click()

# Submits entry and hard sleeps
submitTime = driver.find_element_by_id('submit')
submitTime.click()
time.sleep(2)

# Confirms changes made to the form and quits the driver
confirm = driver.find_element_by_id('confirm_yes')
confirm.click()time.sleep(2)
driver.quit()