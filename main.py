import classes

from settings import  API_KEY

def menu():
	print("1.Total Cases in World")
	print("2.Total Cases in World enter date")
	print("8.Create country file")
	print("9.Exit")
	option=input("Chose option : ")
	if option=="1":
		data=classes.TotalCases()
		data.make_a_call()
	if option=="2":
		data=classes.CasesDailyWorld()
		data.make_a_call()
	if option=="8":
		print(classes.get_list_of_countries())

if __name__=="__main__":
	menu()