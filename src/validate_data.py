import pandas as pd

def validate_data():
    data = pd.read_csv("data/cars_data.csv", sep=';')

    data = data.drop_duplicates()
    data = data.dropna()
    data = data[['make', 'model', 'year', 'mileage', 'engine_power', 'fuel_type', 'gearbox', 'price']]
    data = data[data['mileage'].astype(int) > 1000]
    data = data[data['price'].astype(int) > 1000]
    data = data[data['year'].astype(int) > 1990]

    data.to_csv("data/cleaned_data.csv", index=False, sep=';')

validate_data()