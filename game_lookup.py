#!flask/bin/python
from flask import Flask, jsonify
import top_titles
import unittest

app = Flask(__name__)
scores = top_titles.retrieve()

@app.route('/games/<searchTitle>', methods=['GET'])
def get1Score(searchTitle):
	print searchTitle
	entryList=[]
	entry = {"title": searchTitle, "score": "title not found"}
	for item in scores:
		if item["title"] == searchTitle:
			entry = {"title": item["title"].encode("utf-8"),"score": item["score"].encode("utf-8")}
        entryList.append(entry)
	return jsonify(entryList)

@app.route('/games', methods=['GET'])
def getScores():
	return jsonify(scores)

class scoreTest(unittest.TestCase):
	def test1(self):
		with app.app_context():
			results = getScores()
			self.assertEquals(results.status_code, 200)

	def test2(self):
		with app.app_context():
			results = get1Score("Red Dead Redemption 2")
			self.assertEquals(results.status_code, 200)

	def test3(self):
		with app.app_context():
			results = get1Score("Not a game title")
			self.assertEquals(results.status_code, 200)

if __name__ == '__main__':
	#unittest.main()
	app.run(port=80, debug=True)
