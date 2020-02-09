import requests as req

def K_to_C(temp_F):
    return temp_F - 273.1

def search_by_name(city_name, state=None, country_abbreviation=None):
    respond = {}
    respond['status'] = 'Fail'
    if not type(city_name) == str:
        return respond
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name
    if state!=None and country_abbreviation!=None:
        url = url + ',' + state + ',' + country_abbreviation
    elif state!=None:
        url = url + ',' + state
    elif country_abbreviation!=None:
        url = url + ',' + country_abbreviation
    url = url + '&appid=65fca6cee9f758f6bbabffdd03b8e7d6'
    r = req.get(url)
    if r.status_code != 200:
        return respond
    r = r.json()
    respond['status'] = 'Success'
    respond.update(coord = r['coord'])
    respond.update(weather = r["weather"][0]["main"])
    respond.update(description = r["weather"][0]["description"])
    respond.update(tempreture = K_to_C(r["main"]["temp"]))
    respond.update(temp_min = K_to_C(r["main"]["temp_min"]))
    respond.update(temp_max = K_to_C(r["main"]["temp_max"]))
    respond.update(humidity = r["main"]["humidity"])
    respond.update(wind = r["wind"]["speed"])
    return respond

def search_by_coordinates(latitude, longitude):
    pass

def forecast_by_name(city_name, state=None, country_abbreviation=None):
    pass

def forecast_by_coordinates(latitude, longitude):
    pass

if __name__ == '__main__':
    r = search_by_name('London')
    print(r)