from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import MySQLdb
import os 

dbName = os.environ.get('DB_NAME')
dbUserName = os.environ.get('DB_USER_NAME')
dbUserPassword = os.environ.get('DB_USER_PASSWORD')
dbTableName = os.environ.get('DB_TABLE_NAME')

db= MySQLdb.connect("localhost",dbUserName,dbUserPassword,dbName )
# prepare a cursor object using cursor() method
cursor = db.cursor()


display = Display(visible=0, size=(1,1))
display.start()

def retrieveSell(url):
	browser = webdriver.Firefox()
	browser.get(url)
	htmlSource = browser.page_source

	soup = BeautifulSoup(htmlSource, 'html.parser')
	stuff = soup.findAll('h3')
	print stuff[5].getText()[1:]
	browser.quit()
display.stop()

def urlDecomposition(reqURL):
	val = reqURL.split('/')
	site = val[2]
	brand = val[3]
	model = val[4]
	carrier = val[5]
	capacity = val[6]
	deviceID = val[7]
	print site
	print brand
	print model
	print carrier
	print capacity
	print deviceID
	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO testers(brand, model, carrier, capacity, deviceid)
		 VALUES ('iphone', '6s', 'att', '16gb', '34234')"""
	try:
	   # Execute the SQL command
	   print sql
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()


aurl = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus:-128gb-at-t/496035-gpid"
burl = "https://www.gazelle.com/iphone/iphone-6s-plus/at-t/iphone-6s-plus-16gb-at-t/496033-gpid"
urlDecomposition(aurl)
#retrieveSell(aurl)
#retrieveSell(burl)
#db.close()
