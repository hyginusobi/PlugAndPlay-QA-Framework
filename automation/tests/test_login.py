from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login_flow():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:8080/login")

    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("Passw0rd!")
    driver.find_element(By.ID, "btnLogin").click()

    assert "Dashboard" in driver.title
    driver.quit()
