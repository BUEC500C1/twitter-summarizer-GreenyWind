# API Description
## Functions: 
Users can search the current weather of over 200,000 airports specified by the city name or location (geographic coordinates).
## API interfaces:
1. search_by_name(city_name, state=None, country_abbreviation=None):
    * Parameters:
        * city_name: The name of the city where the airport locates.
        * state (default is None): The state where the airport locates (available only for the USA locations).
        * country_abbreviation (default is None): The country where the airport locates.
    * Return value: A python dictionary object containing the current weather of the airport.
2. search_by_coordinates(latitude, longitude):
    * Parameters:
        * latitude: the latitude of the airport.
        * ongitude: the longitude of the airport.
    * Return value: A python dictionary object containing the current weather of the airport.

## Examples:
1. User story: A user would like to find the current weather in the airport of London.
![search by name](./ "London Airport")
2. User story: A user would like to find the current weather of Newark airport in New York. Yet because there are four airports in New York, he has to use the coordinates to specify the airport he is looking for.
![search by coordinates](./ Newark Airport)

# Implementation
I took advantage of only _OpenWeather API_ but not _National Weather Service API_ to implement my API because it has several disdvantages as shown below:
|                                   | OpenWeather API | National Weather Service API |
| --------------------------------- | --------------- | ---------------------------- |
|         search by name ?          |       Yes       |              No              |
|     searvh by coordinates?        |       Yes       |             Yes              |
| Support coordinates are limited ? |       No        |             Yes              |
