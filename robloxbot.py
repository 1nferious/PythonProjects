from selenium import webdriver
from pynput.mouse import Button, Controller
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://roblox.com/login");
nameBox = driver.find_element_by_id("login-username");
passwordBox = driver.find_element_by_id("login-password");
loginBtn = driver.find_element_by_id("login-button");
robloxfencing = 'https://www.roblox.com/games/12109643/Fencing'
successfullog = 'Home - Roblox'

nameBox.send_keys("test");
passwordBox.send_keys("test");
loginBtn.click();
while driver.title != successfullog:
    pass
else:
    driver.get(robloxfencing)
