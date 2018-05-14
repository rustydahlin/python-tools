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
import requests
import bs4
import time

# User Input for URL
##text_url = input("Please Enter URL: ")
##print(text_url)
##input("If URL looks correct, press ENTER to continue. If not, press CTRL+C")

# Command Line Argument for URL
# Usage: $ python url_text_scraper.py [URL]
##text_url = sys.argv[1]

# Static Text Path
# Example: text_url = "http://bismarck-larks.northwoodsleague.tv/Home/SelectPromoSeats?UserPromoCode=CURL"  
text_url = "http://www.WEBSITE.com"  

# GET request for text scraping
res = requests.get(text_url)

# Set variable for info
info = bs4.BeautifulSoup(res.text, 'html.parser')

# Set variable infoText to store what you are scraping
# Example: infoText = info.select('.promoCodeRow')
# - .promoCodeRow in this example points to the name of several rows in a table on a website - Derived from the CSS
infoText = info.select('.texttoscrape')

# Display output from webpage
# Example: print('There are currently ' + str(len(infoText)) + ' tickets remaining.')
# - str(len(infoText)) adds up how many instances of '.promoCodeRow' it finds, and displays as an integer
print(str(len(infoText)))

# Timeout on CL window to display result before closing
time.sleep(10)