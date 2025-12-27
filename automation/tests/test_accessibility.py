from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login_form_labels():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:8080/login")

    assert driver.find_element(By.XPATH, "//label[@for='username']").is_displayed()
    assert driver.find_element(By.XPATH, "//label[@for='password']").is_displayed()

    driver.quit()
