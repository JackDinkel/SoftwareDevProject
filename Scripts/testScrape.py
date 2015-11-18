
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

display = Display(visible=0, size=(1,1))
display.start()

def retrieveSell(url):
	browser = webdriver.Firefox()
	browser.get(url)
	htmlSource = browser.page_source

	soup = BeautifulSoup(htmlSource, 'html.parser')
	stuff = soup.findAll('h3')
	print stuff
	browser.quit()
aurl = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus:-128gb-at-t/496035-gpid"
burl = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus-16gb-at-t/496033-gpid"
retrieveSell(aurl)
display.stop()
