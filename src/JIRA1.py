from selenium import webdriver
PATH = "A:\Programy\JetBrains\chromdriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://facebook.com")