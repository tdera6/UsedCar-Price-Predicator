import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model():
    data = pd.read_csv("data/cleaned_data.csv", sep=';')

    data_encoded = pd.get_dummies(data, columns=['make', 'model', 'fuel_type', 'gearbox'], drop_first=True)

    X = data_encoded.drop("price", axis=1)
    y = data_encoded["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Mean Absolute Error: {mae}")

    joblib.dump(model, "data/car_price_model.pkl")
    joblib.dump(X_train.columns.tolist(), "data/model_columns.pkl")

if __name__ == "__main__":
    train_model()