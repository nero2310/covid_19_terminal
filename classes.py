import requests
import json
from datetime import date, timedelta

from settings import API_KEY


def get_list_of_countries():  # toDo rewrite save to file
	url = "https://covid-19-data.p.rapidapi.com/help/countries"
	query = {"format": "json"}
	headers = {
		'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
		'x-rapidapi-key': API_KEY
	}
	response = requests.request("GET", url, headers=headers, params=query)
	json_response = json.dumps(response.json())
	with(open("countires.json", "w")) as file:
		for element in json_response:
			file.write(str(element))
	return response.text


class DateAnalyzer:
	def __init__(self, data):
		self.json_obj = data
		self.cases_dict = self.json_obj[0]

	def print_json(self):
		for key, value in self.json_obj[0].items():
			print(key, value)


class BaseApiClass:
	def __init__(self):
		self.date_today = date.today()
		self.yesterday = date.today() - timedelta(days=1)
		self.date_today, self.yesterday = self.date_today.strftime("%Y-%m-%d"), self.yesterday.strftime("%Y-%m-%d")
		self.headers = {
			'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
			'x-rapidapi-key': API_KEY
		}
		self.query = {}
		self.url = ""

	def make_a_call(self):
		self.response = requests.request("GET", self.url, headers=self.headers, params=self.query)
		json_obj = json.loads(self.response.text)
		data_analyzer = DateAnalyzer(json_obj)
		data_analyzer.print_json()


class TotalCases(BaseApiClass, DateAnalyzer):
	def __init__(self):
		super().__init__()
		self.query = {"format": "json"}
		self.url = "https://covid-19-data.p.rapidapi.com/totals"

	def print_headers(self):
		print(self.headers)


class TotalCasesDaily(BaseApiClass, DateAnalyzer):
	def __init__(self):
		super().__init__()
		self.query = {"date-format": "YYYY-MM-DD", "format": "json", "date": self.date_today}
		self.url = "https://covid-19-data.p.rapidapi.com/report/totals"
