from bs4 import BeautifulSoup
import requests

def url_scraper(url):
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        links = []
        for link in soup.find_all("a"):
                links.append(link)
	return links
def scrape_gazelle():
	url = "http://buy.gazelle.com/buy/used/catalog/iphones"
	links = url_scraper(url)
	print links

def scrape_swappa():
	url = "https://swappa.com/buy/iphones"
	links = url_scraper(url)
	print links

def main():
	#print "Which site will you scrape?"
	#scrape_gazelle()
	scrape_swappa()
main()
