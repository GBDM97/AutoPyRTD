from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options)
print(driver.title)
print(driver.find_element(By.ID,"lblAtivoNome_BOOK1").text)

#chrome.exe –remote-debugging-port=9222–user-data-dir=C:\Program Files\Google\Chrome\Application