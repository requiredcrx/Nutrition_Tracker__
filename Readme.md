# Nutrition Tracker

This project is a command-line tool that allows you to track your nutrition by entering the foods you eat. It uses the Nutritionix API to retrieve nutrition information for the foods and then logs the data to a Google Sheet using the Google Sheets API.

## Prerequisites

Before running the program, make sure you have the following:

- Python 3
- Requests library (`pip install requests`)
- Dotenv library (`pip install python-dotenv`) (optional, for hiding sensitive information)
- Google Sheets API credentials (follow the instructions in the "Setup" section)

## Setup

1. Clone the repository or download the script.

2. Create a free account on the [Nutritionix Developer Portal](https://developer.nutritionix.com/) and obtain your API credentials (app ID and API key).

3. Enable the Google Sheets API and create credentials (service account) following the instructions in the [Google Sheets API Python Quickstart Guide](https://developers.google.com/sheets/api/quickstart/python).

4. Save the JSON credentials file as `credentials.json` in the project directory.

5. (Optional) If you want to hide your sensitive information like API keys and credentials, create a `.env` file in the project directory and add the following variables:

##  Example changes in Google Sheet
![Screen Shot 2023-07-17 at 18 21 53](https://github.com/requiredcrx/Nutrition_Tracker__/assets/91392775/d56e5b72-c00e-4f76-9b1c-d0789da909ad)

