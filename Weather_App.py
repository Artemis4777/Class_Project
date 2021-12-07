import requests, json

print("Welcome to the best discount weather app!")

def get_zip(zip_code):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={zip_code}&appid=8ff4487d9dc4a13a3dc17413012d68d7")
    x = response.json()

    
    if x["cod"].lower() == "exit":
        exit = True
    elif x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature = (int(current_temperature) - 273.15) * 9/5 + 32
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in fahrenheit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))

    else:
        print(" City Not Found ")

exit = False
while exit == False:
    answer = input("\nPlease enter your city, or type Exit: ")
    
    if answer == "Exit":
        print("\nOkay, I guess this is goodbye :'(")
        break
    
    else:
        get_zip(answer)