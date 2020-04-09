from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

GOOGLE_LOGIN = "https://google.com"


# logs the user into google
def login_to_google(driver, settings):
    
    # navigate to google.com
    driver.get(GOOGLE_LOGIN)

    # click on the sign in button
    sign_in = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]")
    sign_in.click() 

    # enter email and submit
    driver.find_element_by_id("identifierId").send_keys(settings["email"])
    driver.find_element_by_id("identifierNext").click()

    # maybe a sleep will work?
    time.sleep(2)
    # seems to

    # enter password and submit
    password = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
    )
    password.send_keys(settings["password"])

    driver.find_element_by_id("passwordNext").click()
