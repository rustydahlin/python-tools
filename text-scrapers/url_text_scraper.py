#-------------------------------------------------------------------------------
# Name:        Website Text Scraper
# Purpose:     Reaches out to a URL path, finds the text you are looking for and displays it.
#              Options: User Input; Command Line Argument; Static Path
#              Uses: Scraping remaining available tickets from vendor; 
#                    Displaying commonly changing information from a website.
#
# Author:      rdahlin
#
# Created:     05/13/2018
# Copyright:   (c) rdahlin 2018
# Version:     Python 3.6.5
#-------------------------------------------------------------------------------

# imported libraries
import requests, bs4
import time

# URL for text scraping
res = requests.get('http://bismarck-larks.northwoodsleague.tv/Home/SelectPromoSeats?UserPromoCode=CURL')

# Set variable for info
info = bs4.BeautifulSoup(res.text, 'html.parser')

# Set variable infoText to store what you are scraping
# .promoCodeRow in this example points to the name of several rows in a table on a website
infoText = info.select('.promoCodeRow')

# Display output from webpage
# str(len(infoText)) adds up how many instances of 'promoCodeRow' it finds, and displays as an integer
print('There are currently ' + str(len(infoText)) + ' tickets remaining.')

# Timeout on CL window to display result before closing
time.sleep(10)