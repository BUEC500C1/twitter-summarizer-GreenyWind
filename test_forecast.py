from weather_APIs.apweather import forecast_by_name, forecast_by_coordinates

def test_fail():
	respond = forecast_by_name('New York')
	assert respond['status'] == 'Fail'

	respond = forecast_by_coordinates(1000, 10)
	assert respond['status'] == 'Fail'

def test_success():
	respond = forecast_by_name('London')
	assert respond['status'] == 'Success'

	respond = forecast_by_coordinates(40, 74)
	assert respond['status'] == 'Success'
