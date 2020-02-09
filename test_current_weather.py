from apweather import search_by_name, search_by_coordinates

def test_fail():
	respond = search_by_name('TT')
	assert respond['status'] == 'Fail'

	respond = search_by_coordinates(1000, 10)
	assert respond['status'] == 'Fail'

def test_success():
	respond = search_by_name('London')
	assert respond['status'] == 'Success'

	respond = search_by_coordinates(40, 74)
	assert respond['status'] == 'Success'

if __name__ == "__main__":
	test_fail()
	test_success()