import classes

from settings import API_KEY


def menu():
    print("1.Total Cases in World")
    print("2.Total Cases in World (user specify date)")
    print("3 Total Cases in Country (user specify date)")
    print("4.TESTING send data about total cases to pandas dataframe")
    print("8.Create country file")
    print("9.Exit")
    option = input("Chose option : ")
    if option == "1":
        data = classes.CasesInWorld()
        python_object = data.make_a_call()
        data_analyzer = classes.DateAnalyzer(python_object).print_json()
    if option == "2":
        data = classes.CasesDailyWorld()
        data.set_date(input("Set date from which cases will be displayed example 2020-5-15 "))
        python_object = data.make_a_call()
        data_analyzer = classes.DateAnalyzer(python_object).print_json()
    if option == "3":
        data = classes.CasesDailyCountry()
        data.set_date(input("Set date from which cases will be displayed example 2020-5-15 "))
        python_object = data.make_a_call()
        data_analyzer = classes.DateAnalyzer(python_object).print_provinces()
    if option == "4":
        data = classes.CasesInWorld()
        python_object = data.make_a_call()
        dataFrame = classes.PandasDataAnalyzer(python_object)
        dataFrame.print_data_frame()
        dataFrame.save_to_json("example.json")

    if option == "8":
        print(classes.get_list_of_countries())


if __name__ == "__main__":
    menu()
