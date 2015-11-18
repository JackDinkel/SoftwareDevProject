
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

display = Display(visible=0, size=(1,1))
display.start()


url = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus:-128gb-at-t/496035-gpid"
browser = webdriver.Firefox()
print "getting"
browser.get(url)
htmlSource = browser.page_source

soup = BeautifulSoup(htmlSource, 'html.parser')
stuff = soup.findAll('h3')
print stuff
browser.quit()
burl = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus-16gb-at-t/496033-gpid"
display.stop()
