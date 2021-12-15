#import modules
import requests, json

print("Welcome to the best discount weather app!")

#main function
def get_zip(zip_code):
    try:
#        cnt = input("How many days would you like me to forecast? Please enter "
#        "a number between 1 and 16: ")
#        cnt = int(cnt)
        response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast"
            f"?zip={zip_code},us&units=imperial&appid=8ff4487d9dc4a13a3dc17413012d68d7")
        x = response.json()

    except ConnectionError:
        print("Sorry, it seems that you are not connected to the internet.")

    else:
        if x["cod"] == "200":
#            y = x["main"]
#            current_temperature = y["temp"]
#            current_temperature = (int(current_temperature) - 273.15) * 9/5 + 32
#            current_pressure = y["pressure"]
#            current_humidity = y["humidity"]
#            z = x["weather"]
#            weather_description = z[0]["description"]
#            print(" Temperature (in fahrenheit) = " +
#                    str(current_temperature) +
#              "\n atmospheric pressure (in hPa unit) = " +
#                    str(current_pressure) +
#              "\n humidity (in percentage) = " +
#                    str(current_humidity) +
#              "\n description = " +
#                    str(weather_description) +
#              "\n description = " +
#                    str(weather_description) +
#              "\n description = " +
#                    str(weather_description) +
#              "\n description = " +
#                    str(weather_description))
#            print(x)
            d1_temp_high = x["list"][0]["main"]["temp_max"]
            d1_temp_low = x["list"][0]["main"]["temp_min"]
            d1_temp_info = x["list"][0]["weather"][0]["description"]
            d2_temp_high = x["list"][1]["main"]["temp_max"]
            d2_temp_low = x["list"][1]["main"]["temp_min"]
            d2_temp_info = x["list"][1]["weather"][0]["description"]
            d3_temp_high = x["list"][2]["main"]["temp_max"]
            d3_temp_low = x["list"][2]["main"]["temp_min"]
            d3_temp_info = x["list"][2]["weather"][0]["description"]
            d4_temp_high = x["list"][3]["main"]["temp_max"]
            d4_temp_low = x["list"][3]["main"]["temp_min"]
            d4_temp_info = x["list"][3]["weather"][0]["description"]
            d5_temp_high = x["list"][4]["main"]["temp_max"]
            d5_temp_low = x["list"][4]["main"]["temp_min"]
            d5_temp_info = x["list"][4]["weather"][0]["description"]
            print(f"Tomorrow there will a high of {d1_temp_high}, with a low of"
            f" {d1_temp_low} degrees. There will also be {d1_temp_info}.")
            print(f"On day two there will be a high of {d2_temp_high}, and a"
            f" low of {d2_temp_low} degrees. There will also be {d2_temp_info}.")
            print(f"On day three there will be a high of {d3_temp_high}, and a"
            f" low of {d3_temp_low} degrees. There will also be {d3_temp_info}.")
            print(f"On day four there will be a high of {d4_temp_high}, and a"
            f" low of {d4_temp_low} degrees. There will also be {d4_temp_info}.")
            print(f"On day five there will be a high of {d5_temp_high}, and a"
            f" low of {d5_temp_low} degrees. There will also be {d5_temp_info}.")

        else:
            print(" City Not Found ")

#to keep the program in a loop
exit = False
while exit == False:
    answer = input("\nPlease enter your zip code, or type Exit: ")
    
    if answer == "Exit" or answer == "exit":
        print("\nOkay, I guess this is goodbye :'(")
        exit = True
    
    else:
        get_zip(answer)