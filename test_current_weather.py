from weather_APIs.apweather import search_by_name, search_by_coordinates

def test_search_fail():
	respond = search_by_name('TT')
	assert respond['status'] == 'Fail'

	respond = search_by_coordinates(1000, 10)
	assert respond['status'] == 'Fail'

def test_search_success():
	respond = search_by_name('London')
	assert respond['status'] == 'Success'

	respond = search_by_coordinates(40, 74)
	assert respond['status'] == 'Success'
