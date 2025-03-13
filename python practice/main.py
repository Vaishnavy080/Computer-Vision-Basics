from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("https://www.google.com")

def click_on_element(self, element_xpath):
    element=self.driver.find_element(By.XPATH,element_xpath)
    if element.click():
        return True
    else:
        return False

search_box = driver.find_element(By.XPATH, "")
search.click()
select_link = "xpath"
click_on_element(select_link)


