import urllib2
import unittest

# Return html from a page
def website (page_url):
	# Get the request
	req = urllib2.Request(page_url, headers={"User-Agent" : "Magic Browser"}) 

	# query the website and return the html 
	page = urllib2.urlopen(req)

        return page

class htmlTest(unittest.TestCase):
    def test(self):
	self.assertIn("Example Domain", website("http://example.com").read())

if __name__ == '__main__':
    unittest.main()
