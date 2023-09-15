import json
from web_service_call import WebServiceCall

def main():
    wsc = WebServiceCall()
    json_data = json.loads(wsc.call_service(get_lookup()))
    locations = json_data["Data"]
    for location in locations:
        print(f"City:     {location['City']}")
        print(f"County:   {location['County']}")
        print(f"State:    {location['State']}")
        print(f"Zip Code: {location['ZipCode']}")

def get_lookup():
    return input("Please enter a zip code to look up\n> ")

if __name__ == "__main__":
    main()