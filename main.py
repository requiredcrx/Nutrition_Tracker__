import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# setting up the environment variable
load_dotenv()

# declaring variables to store neccessary informations and geting the environment variables
apiKey = os.getenv("API_KEY")
appID = os.getenv("APP_ID")
EndPoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
SheetEndpoint = os.getenv("SHEET_ENDPOINT")
AuthEndpoint = "https://httpbin.org/basic-auth/user/pass"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


# The try except is used so as to handle errors if user didn't provide an input
try:
    exercise_text = input("What did you eat today?: ")

except KeyboardInterrupt:
    print("\nYou ended the program")
else:

    headers = {
        "x-app-id": appID,
        "x-app-key": apiKey,
        "Content-Type": "application/json"
    }
    parameters = {
        "query": exercise_text,
    }

  
# getting response from Nutritionix API
    response = requests.post(url=EndPoint, headers=headers, json=parameters)
    result = response.json()
    
    today = datetime.now().date()
    today_fmt = today.strftime("%d/%m/%Y")

    time = datetime.now().time()
    time_fmt = time.strftime("%X")

    # basic = HTTPBasicAuth(username="", password="")
    # auth_response = requests.get(url=AuthEndpoint, auth=basic)

    header = {
        "Content-Type": "application/json"
    }

    for food in result["foods"]:
        params = {
            "workout": {
                "date": today_fmt,
                "time": time_fmt,
                "food": food["food_name"],
                "fats": food["nf_total_fat"],
                "calories": food["nf_calories"],
                "cholesterol": food["nf_cholesterol"],
                "sugar": food["nf_sugars"],
                "carbohydrate": food["nf_total_carbohydrate"]
            }
        }
        sheet_response = requests.post(url=SheetEndpoint, json=params, auth=(USERNAME, PASSWORD))
        print(sheet_response.text)

