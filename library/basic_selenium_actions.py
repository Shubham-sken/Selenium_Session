from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def open_browser_to_link(url):
    service = Service("C://Users//SALESKEN//upskill_Learning//Selenium_Session//constants//driver//chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)
    return driver

def wait_until_element_is_visible(driver, xpath, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if element:
            return f"Element found: {xpath}"
    except Exception as e:
        print(f"{e}: Element not found {xpath}")

def click_element(driver, xpath):
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def enter_text_in_element(driver, xpath, text):
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

def select_value_in_dropdown(driver, xpath, value):
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    dropdown = Select(element)
    dropdown.select_by_value(value)

def get_element_text(driver, xpath):
    wait_until_element_is_visible(driver, xpath)
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def scroll_to_element(driver, xpath):
    wait_until_element_is_visible(driver, xpath)
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)

