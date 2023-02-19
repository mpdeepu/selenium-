tit'''
Created on 19-Feb-2023

@author: HP
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
resize=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
action=ActionChains(driver)
action.click_and_hold(resize).move_by_offset(150,0).perform()
header=driver.find_element(By.XPATH,"//h3[@class='ui-widget-header']")
action.click_and_hold(header).move_by_offset(130,0).perform()