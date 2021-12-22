from speak_engine import speak
from microphone import takeInput
import requests

def weather_forcast(text, source):
    api_key="339736107d2cc0843772f9a203922d61"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    city_name = takeInput(source).lower()
    print(city_name)
    
    complete_url = base_url + "appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature =round(y["temp"] - 273.15, 2)
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in celsius unit is " +
            str(current_temperature) +
            "\n humidity in percentage is " +
            str(current_humidiy) +
            "\n description  " +
            str(weather_description))
        print(" Temperature in celsius unit = " +
            str(current_temperature) +
            "\n humidity (in percentage) = " +
            str(current_humidiy) +
            "\n description = " +
            str(weather_description))
