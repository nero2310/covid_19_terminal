import requests

from settings import  API_KEY

def get_list_of_countries():
	url = "https://covid-19-data.p.rapidapi.com/help/countries"
	query={"format":"json"}
	headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }
	response=requests.request("GET",url,headers=headers,params=query)
	return response.text


class HeadersApi:
	def __init__(self):
		self.headers={
	    	'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
	    	'x-rapidapi-key':API_KEY
		}
		self.query={}
		self.url=""
	def make_a_call(self):
		self.response=requests.request("GET",self.url,headers=self.headers,params=self.query)
	def print_data(self):
		self.make_a_call()
		elements=self.response.text.split(",")
		for element in elements:
			print(element)

class TotalCases(HeadersApi):
	def __init__(self):
		super().__init__()
		self.query = {"format": "json"}
		self.url="https://covid-19-data.p.rapidapi.com/totals"
	def print_headers(self):
		print(self.headers)
class TotalCasesDaily(HeadersApi):
	def __init__(self):
		super().__init__()
		self.query={"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-22"}
		self.url="https://covid-19-data.p.rapidapi.com/report/totals"



