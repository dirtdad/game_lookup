import get_html
from bs4 import BeautifulSoup
import unittest

def retrieve():

	metacritic_html = get_html.website("http://www.metacritic.com/game/playstation-4")

	soup = BeautifulSoup(metacritic_html, "html.parser")

	summaries = soup.find_all("td", class_="clamp-summary-wrap")

	entryList=[]
	for summary in summaries:
		title = summary.find("h3").text.strip()
		metascore = summary.find("div", class_="metascore_w large game positive").text.strip()
		entry = {"title": title.encode("utf-8"),"score": metascore.encode("utf-8")}
                entryList.append(entry)
	return entryList

class htmlTest(unittest.TestCase):
    def test(self):
	results = retrieve()
	print results
	self.assertEquals(len(results),10)

if __name__ == '__main__':
    unittest.main()
