# Used Car Price Predictor (ML)

A simple educational project created to estimate used car prices in Poland using machine learning.

## About the Project

This repository contains a set of scripts that form a basic data pipeline:

- **Scraper**: Fetches car listings from a public API.
- **Data Cleaning**: Removes duplicates, missing values, and extreme price/mileage anomalies.
- **Machine Learning**: Prepares the data and trains an `XGBoost` model to predict prices.
- **Web App**: A simple UI built with `Streamlit` to input car parameters and get a price estimate.

## Tech Stack

- Python
- pandas
- scikit-learn
- xgboost
- streamlit

## How to Run Locally

The trained model and column templates are included in the repository (in the `data/` folder), so the app works out of the box.

### 1. Clone the repository

```bash
git clone https://github.com/tdera6/UsedCar-Price-Predicator.git
cd UsedCar-Price-Predicator
```

### 2. Create and activate a virtual environment

**Linux / Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the web app

```bash
streamlit run src/app.py
```

## Project Structure

- `data/` - contains the trained model file (`.pkl`) and cleaned datasets
- `src/scraper.py` - script for fetching listings
- `src/validate_data.py` - data cleaning and preparation
- `src/train_model.py` - variable encoding and XGBoost model training
- `src/app.py` - main user interface file (Streamlit)
- `requirements.txt` - list of required Python packages

## Known Limitations & Future Ideas
* **Accuracy:** The model's average error is around 9000 PLN. This is because it predicts prices based on basic stats (like year, mileage, and engine size). It cannot see the car's actual physical condition, accident history, or premium equipment.
* **UI Input Validation:** Currently, the user interface allows selecting any combination of Make and Model.
