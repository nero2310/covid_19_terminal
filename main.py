import classes

from settings import  API_KEY

def menu():
	print("1.Total Cases in World")
	print("2.Total Cases in today in World")
	print("8.Create country file")
	print("9.Exit")
	option=input("Chose option")
	if option=="1":
		var=classes.TotalCases()
		var.print_data()
	if option=="2":
		var=classes.TotalCasesDaily()
		var.print_data()
	if option=="8":
		print(classes.get_list_of_countries())

menu()