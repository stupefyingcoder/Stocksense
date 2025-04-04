import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('stock_prediction_model.h5')

# Load dataset automatically
df = pd.read_csv('stock_data_long_format.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Get unique stock symbols for dropdown
stock_symbols = df['Stock'].unique().tolist()

# Function to prepare the MinMaxScaler
def prepare_scaler(stock_symbol):
    stock_data = df[df['Stock'] == stock_symbol]['Close'].values.reshape(-1, 1)
    
    if len(stock_data) == 0:
        return None  # No data for this stock symbol
    
    scaler = MinMaxScaler()
    scaler.fit(stock_data)  # Fit the scaler on available stock data
    return scaler

# Function to predict stock price
def predict_stock_price(stock_symbol):
    stock_data = df[df['Stock'] == stock_symbol].sort_values(by="Date", ascending=True)

    if len(stock_data) < 60:
        return "Not enough historical data available for prediction."

    # Select the most recent 60 days
    last_60_days = stock_data['Close'].values[-60:]

    # Prepare the MinMaxScaler for the specific stock
    scaler = prepare_scaler(stock_symbol)
    if scaler is None:
        return "Stock symbol not found in dataset."

    # Reshape and normalize input
    X_input = np.array(last_60_days).reshape(-1, 1)
    X_input = scaler.transform(X_input).reshape(1, 60, 1)

    # Predict the stock price
    predicted_price_scaled = model.predict(X_input)

    # Convert back to original scale
    predicted_price = scaler.inverse_transform(predicted_price_scaled)

    return round(predicted_price[0][0], 2)

# Streamlit UI
st.title("📈Nifty50 Stock Price Predictor")

# Dropdown for stock selection
stock_symbol = st.selectbox("Select Stock Symbol", stock_symbols)

if st.button("Predict"):
    result = predict_stock_price(stock_symbol)
    if isinstance(result, str):  # Error message
        st.warning(result)
    else:
        st.success(f"Predicted Price for {stock_symbol}: ₹{result}")

