import requests

base_url = "https://country-leaders.onrender.com"
country_endpoint = "/countries"
leaders_endpoint = "/leaders"
cookies_endpoint = "/cookie"

session = requests.Session()

def get_countries():
    response = session.get(base_url + country_endpoint)
    return response.json()

def get_leaders(country):
    response = session.get(base_url + leaders_endpoint, params={"country": country})
    return response.json()

def refresh_cookie():
    session.get(base_url + cookies_endpoint)

# Refresh the cookie before making any requests
refresh_cookie()

countries = get_countries()   
# print(f'countries:{countries}') 
leaders_data = {}
for country in countries:
    leaders_data[country] = get_leaders(country)
    
# print(leaders_data)

leader_fr = get_leaders('fr')
print(leader_fr)