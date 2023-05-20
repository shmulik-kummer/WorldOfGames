from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def test_scores_service(url):
    chrome_driver_path = '/home/kummer/Documents/chromedriver'

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Add headless option
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the URL in the browser
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Find the score element in the web page
        score_element = driver.find_element(By.ID, 'score')
        score_text = score_element.text

        # Check if the score is a number between 1 and 1000
        try:
            score = int(score_text)
            return 1 <= score <= 1000
        except ValueError:
            return False
    finally:
        # Quit the driver
        driver.quit()


def test_service(url):
    result = test_scores_service(url)
    if result:
        print("Score value is between 1-1000")
        return 0
    else:
        print("Score value is not in range or N/A")
        return -1


test_service("http://localhost:8777")
