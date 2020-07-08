
from selenium import webdriver
import time

browser = "Chrome"
viewport = "1000X700"
device = "Laptop"

def HackathonReport(task, testName, domId,comparisonResult):
    f = open("traditional-V1-TestResults.txt", "a")

    report_content = "Task: {task}, Test Name: {test_name}, DOM Id: {dom_id}, Viewport: {viewport}, Device: {device}" \
                     ", Status: {status}\n".format(task=task, test_name=testName, dom_id=domId, viewport=viewport,
                                                 device=device, status=comparisonResult)
    f.write(report_content)

    f.close()

    # returns the result so that it can be used for further Assertions in the test code.
    return comparisonResult


webdriver = webdriver.Chrome("C:/Python36/chromedriver.exe")
url = "https://demo.applitools.com/gridHackathonV1.html"

webdriver.get(url)
webdriver.set_window_size(1000, 700)
searchbox = webdriver.find_element_by_xpath('//*[@id="INPUTtext____42"]').is_displayed()
HackathonReport(1, "Search Box is displayed", '//*[@id="INPUTtext____42"]', searchbox)


filter = webdriver.find_element_by_xpath('//*[@id="ti-filter"]').is_displayed()
filter_icon = webdriver.find_element_by_xpath('//*[@id="ti-filter"]')
HackathonReport(2, "Filter is displayed", '//*[@id="ti-filter"]', filter)
filter_icon.click()

black_color_elements = webdriver.find_elements_by_xpath('//*[@class="container_check"]')


for black_color_element in black_color_elements:
    if 'Black' in black_color_element.text:
        black_color_element.click()

filter_option = webdriver.find_element_by_xpath('//*[@id="filterBtn"]').is_displayed()
filter_button = webdriver.find_element_by_xpath('//*[@id="filterBtn"]')
HackathonReport(2, "Filter Box is displayed", '//*[@id="filterBtn"]', filter_option)
filter_button.click()
time.sleep(10)
total_items = webdriver.find_elements_by_xpath('//*[@class="col-6 col-md-4"]')

print("Total items shown:", len(total_items))
if len(total_items) == 2:
    print("Found Black color shoes")
pagelink = total_items[0].find_element_by_tag_name('a').get_attribute('href')
webdriver.get(pagelink)
time.sleep(5)

product_page = webdriver.find_element_by_xpath('//*[@id="shoe_name"]').is_displayed()
HackathonReport(3, "Product page is displayed", '//*[@id="shoe_name"]', product_page)
