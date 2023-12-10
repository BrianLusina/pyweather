import unittest
from pyweather.entities import WeatherData


class WeatherDataTestCase(unittest.TestCase):
    def test_returns_weather_data_from_json(self):
        """should return True if the wrong guesses equals the maximum allowed wrong guesses"""
        weather_id = 6
        city = "example"
        description = "Really Hot Today"
        temperature = 10.0

        data = {
            "name": city,
            "weather": [
                {
                    "id": weather_id,
                    "description": description
                }
            ],
            "main": {
                "temp": temperature
            },
        }

        actual = WeatherData.from_json(data)

        self.assertEqual(city, actual.city)
        self.assertEqual(weather_id, actual.weather_id)
        self.assertEqual(description, actual.description)
        self.assertEqual(temperature, actual.temperature)


if __name__ == '__main__':
    unittest.main()
