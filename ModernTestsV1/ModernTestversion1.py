from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import time

from applitools.selenium import (
    logger,
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)


def set_up(eyes):

    # You can get your api key from the Applitools dashboard
    APPLITOOLS_API_KEY = 'ayj74J3VDMUJn5Mlz7LFcqGQbRg6g0k0uSPMqdezVCE110'
    eyes.configure.set_api_key(APPLITOOLS_API_KEY)

    eyes.configure.set_batch(BatchInfo("UFG Hackathon"))

    (
        eyes.configure.add_browser(1200, 700, BrowserType.CHROME)
        .add_browser(1200, 700, BrowserType.FIREFOX)
        .add_browser(1200, 700, BrowserType.EDGE_CHROMIUM)
        .add_browser(768, 700, BrowserType.CHROME)
        .add_browser(768, 700, BrowserType.FIREFOX)
        .add_browser(768, 700, BrowserType.EDGE_CHROMIUM)
        .add_device_emulation(DeviceName.iPhone_X)
    )

def ultra_fast_test_task1(webdriver, eyes):
    try:

        # Call Open on eyes to initialize a test session
        eyes.open(webdriver, "Applitools", "Task 1", {"width": 800, "height": 600})

        eyes.check("Cross-Device Elements Test", Target.window().fully().with_name("Home page"))

        webdriver.find_element_by_xpath('//*[@id="INPUTtext____42"]')

        # Call Close on eyes to let the server know it should display the results
        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)

def ultra_fast_test_task2(webdriver, eyes):
    try:
        # Call Open on eyes to initialize a test session
        eyes.open(webdriver, "Applitools", "Task 2", {"width": 800, "height": 600})
        filter = webdriver.find_element_by_xpath('//*[@id="ti-filter"]')
        filter.click()
        time.sleep(5)
        black_color_elements = webdriver.find_elements_by_xpath('//*[@class="container_check"]')
        for black_color_element in black_color_elements:
            if 'Black' in black_color_element.text:
                black_color_element.click()
        filter = webdriver.find_element_by_xpath('//*[@id="filterBtn"]')
        filter.click()
        time.sleep(5)

        total_items = webdriver.find_elements_by_xpath('//*[@class="col-6 col-md-4"]')
        eyes.check("Filter Results", Target.window().fully().with_name("Filter page"))

        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)

def ultra_fast_test_task3(webdriver, eyes):
    try:
        # Call Open on eyes to initialize a test session
        eyes.open(web_driver, "Applitools", "Task 3", {"width": 800, "height": 600})


        filter = webdriver.find_element_by_xpath('//*[@id="ti-filter"]')
        filter.click()
        time.sleep(5)
        black_color_elements = webdriver.find_elements_by_xpath('//*[@class="container_check"]')
        for black_color_element in black_color_elements:
            if 'Black' in black_color_element.text:
                black_color_element.click()
        filter = webdriver.find_element_by_xpath('//*[@id="filterBtn"]')
        filter.click()
        time.sleep(5)

        total_items = webdriver.find_elements_by_xpath('//*[@class="col-6 col-md-4"]')


        pagelink = total_items[0].find_element_by_tag_name('a').get_attribute('href')
        webdriver.get(pagelink)

        webdriver.find_element_by_xpath('//*[@id="shoe_name"]')
        time.sleep(5)
        eyes.check("Product Details test", Target.window().fully().with_name("product page"))

        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)


def tear_down(web_driver, runner):
    # Close the browser
    web_driver.quit()

    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


# Create a new chrome web driver
web_driver = Chrome(ChromeDriverManager().install())

# Create a runner with concurrency of 1
runner = VisualGridRunner(10)

# Create Eyes object with the runner, meaning it'll be a Visual Grid eyes.
eyes = Eyes(runner)

set_up(eyes)

try:
    web_driver.get("https://demo.applitools.com/gridHackathonV1.html")
    ultra_fast_test_task1(web_driver, eyes)
    ultra_fast_test_task2(web_driver, eyes)
    ultra_fast_test_task3(web_driver, eyes)
finally:
    tear_down(web_driver, runner)