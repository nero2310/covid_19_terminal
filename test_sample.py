import pytest

import classes

json_obj=[
	{
		"total":15,
		"deaths":200
	}
]

def test_DateAnalyzer():
	assert classes.DateAnalyzer(json_obj).print_json()==1


def test_init_settings():
	pass