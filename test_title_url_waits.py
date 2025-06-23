from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_title_url_waits():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    wait =WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dynamic_loading"))
    wait.until(EC.title_is("The Internet"))

    assert "dynamic_loading" in driver.current_url
    assert driver.title == "The Internet"

    driver.quit()
