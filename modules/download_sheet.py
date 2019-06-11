from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time


# download the appropriate CSV data for this month's attendance
def download_sheet(driver, settings):

    # navigate to the google doc, then wait 5 seconds for it to load
    driver.get(settings["doc_location"])
    time.sleep(5)

    # navigate to the correct sheet based on Month and Year eg. June 2019
    tab_name = datetime.now().strftime("%B %Y")
    tab_element = "//*[contains(text(), '{}')]".format(tab_name)
    driver.find_element_by_xpath(tab_element).click()

    # click on the "Files" element in the ui
    driver.find_element_by_id("docs-file-menu").click()
    time.sleep(1)

    # hover over the "Download as" element in the dropdown
    download_as = driver.find_element_by_xpath("//span[@aria-label='Download as d']")
    ActionChains(driver).move_to_element(download_as).perform()
    time.sleep(1)

    # click the download as csv link in the second dropdown
    csv_label = "//span[@aria-label='Comma-separated values (.csv, current sheet) c']"
    driver.find_element_by_xpath(csv_label).click()
    time.sleep(1)
