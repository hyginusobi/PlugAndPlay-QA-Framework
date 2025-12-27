from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.TAG_NAME, "h1")

    def is_dashboard_loaded(self):
        header = self.driver.find_element(*self.dashboard_header)
        return "Dashboard" in header.text
