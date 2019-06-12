from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

START_URL = "http://learn.codingdojo.com"
ATTENDANCE_URL = "http://learn.codingdojo.com/admin/attendance"
ELEMENT = "//label[@data-original-title='Click this to mark the student {} in all period.']"
# an explanation of the Tysons Corner attendance keys
# a - attended from algorithms onward
# l - attended from after algorithms onward
# d - attended from after lecture onward
# x - unexcused absence
# k - excused absence
# their translation into the keys used by learn.codingdojo.com
KEYS = {
    "a": "Present",
    "l": "Late",
    "d": "Late",
    "x": "Absent",
    "k": "Excused Absence" 
}


# handle inputting current student attendance to the learn platform
def update_attendance(driver, settings, student_data):

    # navigate to the codingdojo learn platform
    driver.get(START_URL)

    # login using email and password
    driver.find_element_by_id("enter_email").send_keys(settings["email"])
    driver.find_element_by_id("enter_password").send_keys(settings["password"])
    driver.find_element_by_id("login_button").click()
    time.sleep(5)

    # navigate to the attendance page
    driver.get(ATTENDANCE_URL)
    time.sleep(5)

    # suppress alerts generated by learn.codingdojo.com
    # based on a setting in settings.json
    if settings["suppress_alerts"]:
        driver.execute_script("window.alert = function(){}")

    # loop through the student data
    for student in student_data:

        # check if attendance data exists for this student
        if student["status"] in KEYS:
            
            # search for the student
            search = driver.find_element_by_id("search_attendance_students_input")
            search.clear()
            search.send_keys(student["email"])
            driver.find_element_by_xpath("//*[contains(text(), 'Fetch')]").click() 
            time.sleep(1)

            # find the appropriate element based on student status
            to_click = driver.find_element_by_xpath(ELEMENT.format(KEYS[student["status"]]))
            # move the mouse over the right element
            action = ActionChains(driver).move_to_element(to_click)
            # click to update the status
            action.click()
            action.perform()
            time.sleep(1)
