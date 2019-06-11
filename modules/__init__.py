from selenium import webdriver
from .download_sheet import download_sheet
from .login_to_google import login_to_google
from .read_sheet import read_sheet
from .update_attendance import update_attendance
import os, json, getpass 

# Calculates the project path (stolen shamelessly from django settings.py)
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Reading in the settings from settings.json
SETTINGS = {}
with open(os.path.join(CURRENT_PATH, "settings.json")) as file:
    SETTINGS = json.loads(file.read())

# So I don't have to store password as plain text!
password = getpass.getpass()
SETTINGS["password"] = password

# basic firefox profile prevents confirmation dialog when downloading
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
profile.set_preference("dom.webnotifications.enabled", False)

# create our webdriver instance
DRIVER = webdriver.Firefox(profile)

# configure it to TimeoutException if any request takes too long (configurable)
DRIVER.set_page_load_timeout(SETTINGS["page_load_timeout"])