from weather_APIs/apweather import search_by_name, search_by_coordinates

def test_not_exist():
	respond = search_by_name('New York')
	assert respond['status'] == 'Fail'

	respond = search_by_coordinates(1000, 10)
	assert respond['status'] == 'Fail'

def test_success():
	respond = search_by_name('London')
	assert respond['status'] == 'Success'

	respond = search_by_coordinates(40, 74)
	assert respond['status'] == 'Success'