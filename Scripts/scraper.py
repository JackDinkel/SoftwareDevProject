from bs4 import BeautifulSoup
import requests
import urllib
###################################################################
Reference Scraper
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
Gazelle
###################################################################
def scrape_gazelle(iphoneModel, carrier, capacity):
	url = "http://buy.gazelle.com/buy/used/catalog/iphones"
	links = url_scraper(url)
	print links

###################################################################
Swappa
###################################################################
def scrape_swappa():
	url = "https://swappa.com/buy/iphones"
	links = url_scraper(url)
	print links

###################################################################
USell
###################################################################

def main():
	#print "Which site will you scrape?"
	scrape_gazelle()
	#scrape_swappa()
main()
