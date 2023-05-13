# Zaimportowanie kodu
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Stwórz obiekt na bazie klasy
driver = webdriver.Chrome()
# Maksymalizacja okna
driver.maximize_window()
# Otwórz stronę
driver.get("https://duckduckgo.com/")
element = driver.find_element(By.ID, "search_form_input_homepage")
element.click()
element.send_key("Czy Tester na WSB jest faktycznie Merito?")
element.submit()
sleep(10)