import requests

def get_website_status(url: str):
    return requests.get(url).status_code

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
status_code = get_website_status(url)

if status_code == 200:
    print(f"The website {url} exists.")
else:
    print(f"The website {url} does not exist. Status code: {status_code}")
    