from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
file = 0
query = "laptop"
for i in range (1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2PE3NWMB9DUYX&qid=1732032941&sprefix=laptops%2Caps%2C111&ref=sr_pg_2")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w",encoding= "utf-8") as f:
            f.write(d)
            file+=1

    time.sleep(2)
driver.close()