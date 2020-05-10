import classes

from settings import API_KEY


def menu():
	print("1.Total Cases in World")
	print("2.Total Cases in World (user specify date)")
	print("3 Total Cases in Country")
	print("8.Create country file")
	print("9.Exit")
	option = input("Chose option : ")
	if option == "1":
		data = classes.TotalCases()
		python_object=data.make_a_call()
		data_analyzer=classes.DateAnalyzer(python_object).print_json()
	if option == "2":
		data = classes.CasesDailyWorld()
		python_object=data.make_a_call()
		data_analyzer=classes.DateAnalyzer(python_object).print_json()
	if option == "3":
		data = classes.CasesDailyCountry()
		data.make_a_call()
	if option == "8":
		print(classes.get_list_of_countries())


if __name__ == "__main__":
	menu()
