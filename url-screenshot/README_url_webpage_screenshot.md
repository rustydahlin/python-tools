Selenium requires a driver to interface with the browser. Selenium can easily be installed by pip.


--------------------------------------------------
Mac:

 Install phantomJS via your package manager or npm. 
 
On OSX, it's just a matter of doing:

brew install phantomjs  
or 
npm -g phantomjs 

--------------------------------------------------
Windows:

Using the Chrome Driver. Download it from: https://sites.google.com/a/chromium.org/chromedriver/downloads
and put it in your PATH so it can be accessed from anywhere.

In my case the driver is located in /usr/local/bin/chromedriver

--------------------------------------------------

You can either save the screenshot on the disk:

driver.save_screenshot(IMAGE_PATH)

or get the screenshot as a binary data:

driver.get_screenshot_as_png()