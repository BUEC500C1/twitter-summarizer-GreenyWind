from weather_APIs.apweather import forecast_by_coordinates

def test_fail():
	respond = forecast_by_coordinates(74, 10)
	assert respond['status'] == 'Fail'

def test_success():
	respond = forecast_by_coordinates(39.7456, -97.0892)
	assert respond['status'] == 'Success'