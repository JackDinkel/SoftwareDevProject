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
import os

dbName = os.environ.get('DB_NAME')
dbUserName = os.environ.get('DB_USER_NAME')
dbUserPassword = os.environ.get('DB_USER_PASSWORD')
dbTableName = os.environ.get('DB_TABLE_NAME')

display = Display(visible=0, size=(1,1))
display.start()
browser = webdriver.Firefox()
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
#Requests+beautifulsoup based
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
def scrape_gazelle(reqURL):
        browser.get(reqURL)
        htmlSource = browser.page_source
	scrape_timestamp = timestamp()
        soup = BeautifulSoup(htmlSource, 'html.parser')
        devicePrice = soup.findAll('h3')
        itemPrice = int(devicePrice[5].getText()[1:])
	siteScrape = urlDecomposition(reqURL)
	insert_to_db(siteScrape[0],siteScrape[1],siteScrape[2],siteScrape[3],"good",itemPrice,siteScrape[4],scrape_timestamp)

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
		scrape_gazelle(reqURL)
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
	'''
	print reqURL
        print site
        print brand
        print model
        print carrier
        print capacity
        print deviceID
	'''
	return brand, model, capacity, carrier, site

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
def insert_to_db(resBrand, resModel, resCapacity, resCarrier, resCondition, resPrice, resSite, resTimestamp):
	db= MySQLdb.connect("localhost", dbUserName, dbUserPassword, dbName)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = """INSERT INTO %s(brand, model, capacity, carrier, item_condition, price, site, timestamp) VALUES ('%s', '%s','%s','%s','%s','%i','%s','%s')"""%(dbTableName, resBrand, resModel, resCapacity, resCarrier, resCondition, resPrice, resSite, resTimestamp)
	
	print sql
        try:
	   print "executing"
           # Execute the SQL command
           cursor.execute(sql)
	   
           # Commit your changes in the database
	   print "commiting"
           db.commit()
        except:
	   print "rolling back"
           # Rollback in case there is any error
           db.rollback()
	db.close()
	#print resBrand, resModel, resCapacity, resCarrier, resCondition, resPrice, resSite, resTimestamp
	
###################################################################
#Main
###################################################################
def main():
	if len(sys.argv) > 1:
		cmdLineTest()
	#print "Which site will you scrape?"
	#scrape_gazelle("6s-plus", "at-t", "16gb")
	#scrape_swappa()
	#print dbName, dbTableName, dbUserName, dbUserPassword
main()
browser.quit()
display.stop()
