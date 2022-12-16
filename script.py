from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.kubii.fr/")

search_field = driver.find_element(By.ID, 'search_query_top')
search_field.send_keys('Rassberry')

search_btn = driver.find_element(By.CLASS_NAME, "button-search")
search_btn.click()

all_titles = driver.find_element(By.CLASS_NAME, "product-name")

# for a in all_titles:
#     print a.get_attribute('title')