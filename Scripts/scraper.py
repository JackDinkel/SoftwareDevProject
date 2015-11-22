from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import requests
import MySQLdb
import urllib
import sys



###################################################################
#Timestamp
###################################################################
def timestamp():
	d = datetime.datetime.now()
	#Timestamp name is year, month, day, hour, minute, second, microsecond in the following numeric setup 4,2,2,2,2,2,6
	return str('{:04d}'.format(getattr(d, 'year')))+str('{:02d}'.format(getattr(d, 'month')))+str('{:02d}'.format(getattr(d, 'day')))+str('{:02d}'.format(getattr(d, 'hour')))+str('{:02d}'.format(getattr(d, 'minute')))+str('{:02d}'.format(getattr(d, 'second')))+str('{:06d}'.format(getattr(d, 'microsecond')))

###################################################################
#Reference Scraper
###################################################################
'''
url = ""
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

for tag in soup.findAll(''):
        print tag
        imgUrl = tag.get('src')
        imgName = imgUrl[imgUrl.rfind('/')+1:]
        #urllib.URLopener().retrieve(imgUrl, imgName)
        try:
                urllib.URLopener().retrieve(imgUrl, imgName)
        except (IOError):
                pass
'''

###################################################################
#Gazelle
###################################################################
#Example url:
#https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus-16gb-at-t/496033-gpid
def scrape_gazelle(iphoneModel, carrier, capacity):
	'''
	url = "http://buy.gazelle.com/buy/used/catalog/iphones"
	links = url_scraper(url)
	print links
	'''
	'''
	url = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus-16gb-at-t/496033-gpid"
	r = requests.get(url)
	#print r
	data = r.text
	#print data
	soup = BeautifulSoup(data, "html.parser")
	#print soup
	#print iphoneModel, carrier, capacity
	#for tag in soup.findAll('span',{'data':'oldoffer'}):
	for tag in soup.findAll('h3'):
		print tag
	'''
	browser = webdriver.Firefox()
        browser.get(url)
        htmlSource = browser.page_source

        soup = BeautifulSoup(htmlSource, 'html.parser')
        stuff = soup.findAll('h3')
        print stuff[5].getText()[1:]
        browser.quit()

###################################################################
#Swappa
###################################################################
def scrape_swappa():
	url = "https://swappa.com/buy/iphones"
	links = url_scraper(url)
	print links

###################################################################
#USell
###################################################################
def scrape_usell():
        url = "https://swappa.com/buy/iphones"
        links = url_scraper(url)
        print links

###################################################################
#URL Sorting
###################################################################
def urlSort(reqURL):
	if "gazelle" in reqURL:
		#print "zomg %s contains gazelle", reqURL
		urlDecomposition(reqURL)
	elif "swappa" in reqURL:
		print "zomg %s contains swappa", reqURL
	elif "usell" in reqURL:
		print "zomg %s contains usell", reqURL
	else:
		print "%s isn't valid for this scraper.", reqURL

###################################################################
#URL Decomposition
###################################################################
def urlDecomposition(reqURL):
        val = reqURL.split('/')
        site = val[2]
        brand = val[3]
        model = val[4]
        carrier = val[5]
        capacity = val[6]
        deviceID = val[7]
	print reqURL
        print site
        print brand
        print model
        print carrier
        print capacity
        print deviceID

###################################################################
#Command Line File Testing
###################################################################
def cmdLineTest():
	numberOfFiles = len(sys.argv)
	argFile = 1
	while argFile < numberOfFiles:
		f = open(sys.argv[argFile],'r')
		for line in f:
			urlSort(line)
		argFile = argFile + 1

###################################################################
#Database Insertion
###################################################################
#DB Table format
#brand|model|capacity|carrier|condition|price|site|timestamp
def insert_to_db(brand, model, capacity, carrier, condition, price, site, timestamp):
	db= MySQLdb.connect("localhost","user","pass","db" )
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
        sql = """INSERT INTO testers(brand, model, carrier, capacity, deviceid)
                 VALUES ('iphone', '6s', 'att', '16gb', '34234')"""
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
	db.close()
	
###################################################################
#Main
###################################################################
def main():
	if len(sys.argv) > 1:
		print "so you wanna do testing with files. eh?"
		cmdLineTest()
	#print "Which site will you scrape?"
	#scrape_gazelle("6s-plus", "at-t", "16gb")
	#scrape_swappa()
main()
