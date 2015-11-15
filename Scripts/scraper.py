from bs4 import BeautifulSoup
import requests
import urllib

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
#Database Insertion
###################################################################
#DB Table format
#brand|model|capacity|carrier|condition|price|site|timestamp
def insert_to_db(brand, model, capacity, carrier, condition, price, site, timestamp):
	x = 0 #Place holder
	
###################################################################
#Main
###################################################################
def main():
	#print "Which site will you scrape?"
	scrape_gazelle("6s-plus", "at-t", "16gb")
	#scrape_swappa()
main()
