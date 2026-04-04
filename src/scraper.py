import requests
import pandas as pd
import random
import time

SAVE_URL = "data/cars_data.csv"
PAGES = 7000

def get_car_data_from_url(max_pages=PAGES):

    page_number = 1
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    cars_data = []

    for i in range(1, max_pages + 1):
        try:
            page_number = i
            url = f"https://www.otomoto.pl/graphql?operationName=listingScreen&variables=%7B%22after%22%3Anull%2C%22experiments%22%3A%5B%7B%22key%22%3A%22MCTA-1463%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22key%22%3A%22CARS-80473%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22key%22%3A%22CARS-80474%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22key%22%3A%22CARS-81954%22%2C%22variant%22%3A%22b%22%7D%2C%7B%22key%22%3A%22CARS-64661%22%2C%22variant%22%3A%22b%22%7D%5D%2C%22filters%22%3A%5B%7B%22name%22%3A%22category_id%22%2C%22value%22%3A%2229%22%7D%5D%2C%22includeCepik%22%3Atrue%2C%22includeFiltersCounters%22%3Afalse%2C%22includeNewPromotedAds%22%3Afalse%2C%22includePremiumTopAd%22%3Afalse%2C%22includePriceEvaluation%22%3Atrue%2C%22includePromotedAds%22%3Afalse%2C%22includeRatings%22%3Afalse%2C%22includeSortOptions%22%3Afalse%2C%22includeSuggestedFilters%22%3Afalse%2C%22maxAge%22%3A60%2C%22page%22%3A{page_number}%2C%22parameters%22%3A%5B%22make%22%2C%22offer_type%22%2C%22show_pir%22%2C%22fuel_type%22%2C%22gearbox%22%2C%22country_origin%22%2C%22mileage%22%2C%22engine_capacity%22%2C%22engine_code%22%2C%22engine_power%22%2C%22first_registration_year%22%2C%22model%22%2C%22version%22%2C%22year%22%5D%2C%22promotedInput%22%3A%7B%7D%2C%22searchTerms%22%3A%5B%5D%2C%22sortBy%22%3A%22relevance_web%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%22882d8ec6a66393b2fa72842a707b38c3f4efbbd63d10edb2f4d40b773c344adf%22%2C%22version%22%3A1%7D%7D"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()

                for car in data["data"]["advertSearch"]["edges"]:
                    
                    car_info = car["node"]

                    car_json = {}

                    car_price = car_info["price"]["amount"]["units"]
                    car_parameters = car_info["parameters"]

                    car_json["price"] = car_price

                    for parameter in car_parameters:

                        if parameter["key"] == "make":
                            make = parameter["value"]
                        elif parameter["key"] == "model":
                            model = parameter["value"]
                        elif parameter["key"] == "year":
                            year = parameter["value"]
                        elif parameter["key"] == "mileage":
                            mileage = parameter["value"]
                        elif parameter["key"] == "engine_power":
                            engine_power = parameter["value"]
                        elif parameter["key"] == "fuel_type":
                            fuel_type = parameter["value"]
                        elif parameter["key"] == "gearbox":
                            gearbox = parameter["value"]

                    car_json["make"] = make
                    car_json["model"] = model
                    car_json["year"] = year
                    car_json["mileage"] = mileage
                    car_json["engine_power"] = engine_power
                    car_json["fuel_type"] = fuel_type
                    car_json["gearbox"] = gearbox

                    cars_data.append(car_json)
            else:
                print(f"Błąd podczas pobierania danych z URL: {response.status_code}")


            if page_number % 50 == 0:
                temp_df = pd.DataFrame(cars_data)
                temp_df = temp_df[['make', 'model', 'year', 'mileage', 'engine_power', 'fuel_type', 'gearbox', 'price']]
                temp_df.to_csv(f"data/backup.csv", index=False, sep=";")

            print(f"Postęp strony {page_number}/{max_pages} - {(page_number/max_pages) * 100:.2f}%")

            time.sleep(0.1)
            
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            time.sleep(5)
            continue

    final_df = pd.DataFrame(cars_data)
    final_df = final_df[['make', 'model', 'year', 'mileage', 'engine_power', 'fuel_type', 'gearbox', 'price']]
    final_df = final_df[final_df['mileage'].astype(int) > 1000]
    final_df.to_csv(SAVE_URL, index=False, sep=";")
    

if __name__ == "__main__":
    get_car_data_from_url(PAGES)