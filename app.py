import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sites import *

driver = webdriver.Firefox()
switch = False

def loginRequired():
	return "Log In" in driver.title

def goToSite(switch):
	index = int(switch)
	data = sites[index]
	
	driver.get(data['url'])
	if loginRequired(): 
		user_login = driver.find_element_by_id('user_login')
		user_login.clear()
		user_login.send_keys(data['username'])

		user_pass = driver.find_element_by_id('user_pass')
		user_pass.clear()
		user_pass.send_keys(data['password'])
		driver.find_element_by_id('wp-submit').click()

	timeOnSite = data['delay'] * 60
	time.sleep(timeOnSite)

driver.fullscreen_window()
while True:
	goToSite(switch)
	switch = not switch