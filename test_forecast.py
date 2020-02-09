from weather_APIs.apweather import forecast_by_name, forecast_by_coordinates

def test_forecast_fail():
	respond = forecast_by_name('TT')
	assert respond['status'] == 'Fail'

	respond = forecast_by_coordinates(1000, 10)
	assert respond['status'] == 'Fail'

def test_forecast_success():
	respond = forecast_by_name('London')
	assert respond['status'] == 'Success'

	respond = forecast_by_coordinates(40, 74)
	assert respond['status'] == 'Success'
