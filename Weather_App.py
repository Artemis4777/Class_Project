import requests

print("Welcome to the best discount weather app!")

def get_zip(zip_code):
    zip_code = input("\nPlease enter your zip code: ")
    requests.get(f"http://api.openweathermap.org/data/2.5/forecast"
        f"?id={zip_code}&appid=8ff4487d9dc4a13a3dc17413012d68d7")

