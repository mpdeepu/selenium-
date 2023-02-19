'''
Created on 19-Feb-2023

@author: MP
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
upload=driver.find_element(By.XPATH,"////input[@id='RESULT_FileUpload-10']")
upload.click()
uploadElement.sendkeys("C:\Users\HP\Downloads\selenium_python.html")
action=ActionChains(driver)
#action.click_and_hold(slider).move_by_offset(150,0).perform()
