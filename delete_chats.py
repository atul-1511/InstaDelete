from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/atukumar4/Desktop/InstaDelete/chromedriver')

driver.get("https://www.instagram.com/")

username = 'iatul.in'
password = 'iitkharagpur'

sleep(3)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
sleep(3)

driver.find_element_by_xpath("//button[contains(.,'Not now')]").click()
sleep(3)

driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()

driver.find_element_by_class_name("xWeGp").click()

try :
    while(1):
        driver.find_element_by_class_name("DPiy6.Igw0E.IwRSH.eGOV_._4EzTm").click()
        #sleep(1)
        info_button = driver.find_elements_by_class_name("wpO6b.ZQScA")
        info_button[1].click()
        #sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Delete Chat')]").click()
        #sleep(1) 
        
        driver.find_element_by_class_name("aOOlW.-Cab_ ").click()
        #sleep(1)
        
except:
    print("All Chats Deleted")