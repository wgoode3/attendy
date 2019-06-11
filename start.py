from modules import DRIVER, SETTINGS
import modules

# log into google using codingdojo email
modules.login_to_google(DRIVER, SETTINGS)

# download the attendance sheet as csv
modules.download_sheet(DRIVER, SETTINGS)

# move the sheet from downloads to 
student_data = modules.read_sheet()

# using student data update the attendance on the learn platform
modules.update_attendance(DRIVER, SETTINGS, student_data)

# quit the webdriver instance when we're all done!
DRIVER.quit()