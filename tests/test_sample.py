import classes.api_handler
from classes import classes

json_obj = [{"total": 15, "deaths": 200}]

cases_dict = [{"confirmed": 0, "recovered": 0}]

cases_dict_2 = [{"confirmed": 0, "recovered": 2}]

cases_dict_3 = [{"confirmed": 1, "recovered": 2}]


def test_date_analyzer():
    assert classes.api_handler.DataPrinter(json_obj).print_json() == 1
    assert classes.api_handler.DataPrinter(cases_dict).cases_validity() == False
    assert classes.api_handler.DataPrinter(cases_dict_2).cases_validity() == True
    assert classes.api_handler.DataPrinter(cases_dict_3).cases_validity() == True


def test_init_settings():
    pass
