#-------------------------------------------------------------------------------
# Name:        Webpage Screenshot
# Purpose:     Reaches out to a URL path, and screenshots the webpage
#              Options: User Input; Command Line Argument; Static Path
#              Options: Screenshot entire webpage; Screenshot portion of webpage
#
# Prerequisites: You must install a webdriver for selenium to use. Check out the README for more information.
#
# Author:      rdahlin
#
# Created:     05/15/2018
# Copyright:   (c) rdahlin 2018
# Version:     Python 3.6.5
#-------------------------------------------------------------------------------

# Import from Static Website Path
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # set the window size that you need 
driver.get('https://github.com') # URL of webpage to be screenshot
driver.save_screenshot('github.png') # path of where to save the screenshot with image name

# Using Chrome Webdriver
##DRIVER = 'chromedriver'
##driver = webdriver.Chrome(DRIVER)
##driver.get('https://www.spotify.com')
##screenshot = driver.save_screenshot('my_screenshot.png')
##driver.quit()