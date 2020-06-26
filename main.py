from classes import pandas_data
from classes import classes
from classes import database_connector

def menu():
    choice=int(input('''
Main Menu
1.Total Cases in World
2.Total Cases in World (user specify date)
3 Total Cases in Country (user specify date)
4.TESTING send data about total cases to pandas dataframe
5.TESTING send data to MongoDB
8.Create country file
9.Exit 
:'''))
    if choice == 1:
        data = classes.CasesInWorld()
        json_object = data.make_a_call()
        data_analyzer = classes.DataPrinter(json_object).print_json()
    if choice == 2:
        data = classes.CasesDailyWorld()
        data.set_date(
            input("Set date from which cases will be displayed example 2020-5-15 ")
        )
        json_object = data.make_a_call()
        data_analyzer = classes.DataPrinter(json_object).print_json()
    if choice == 3:
        data = classes.CasesDailyCountry()
        data.set_date(
            input("Set date from which cases will be displayed example 2020-5-15 ")
        )
        json_object = data.make_a_call()
        each_or_summary = input(
            "Do you wanna see cases in country or cases in regions like states etc.?"
        )
        if each_or_summary == "1" or each_or_summary == "regions":
            data_analyzer = classes.DataPrinter(json_object).print_provinces()
        elif each_or_summary == "2" or each_or_summary == "country":
            data_analyzer = classes.DataPrinter(
                json_object
            ).print_json()  # toDo  output the data in a condensed form

    if choice == 4:
        data = classes.CasesInWorld()
        json_object = data.make_a_call()
        data_frame = pandas_data.PandasDataAnalyzer(json_object)
        data_frame.print_data_frame()
        data_frame.save_to_json("example.json")

    if choice == 5:
        data = classes.CasesInWorld()
        json_object = data.make_a_call()
        connection = database_connector.SaveDataToMongo()
        is_connection_correct = connection.init_connection()
        if is_connection_correct:
            if connection.insert_data(json_object):
                print("Data was insert into db")
        else:
            print("Connection Failure")

    if choice == 8:
        print(classes.get_list_of_countries())

    if choice == 9:
        return False

    return True


if __name__ == "__main__":
    loop = True
    while loop:
        loop = menu()
