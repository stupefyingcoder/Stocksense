# 📈 Stock Price Prediction App

An interactive **Streamlit-based web app** to predict stock prices using **LSTM (Long Short-Term Memory)** models on historical data of NIFTY 50 companies. This project demonstrates the use of deep learning for time-series forecasting in the Indian stock market.

---

## 🚀 Live Demo

🔗 [Click here to try the app](https://stocksense-app.streamlit.app/)

---

## 🧠 About the Project

This project predicts future stock prices using machine learning, specifically LSTM models trained on historical NIFTY 50 stock data. It allows users to select a stock, view its historical trends, and generate predictions.

### ✅ Features

- 📊 Stock price visualization
- 🔮 Predict future stock prices using LSTM
- 📈 Dynamic charts powered by Plotly
- 🧠 Trained TensorFlow model included
- 🧾 Easy-to-use UI with Streamlit

---

## 🗂️ Project Structure

```
📦 STOCK_PRICE/
├── .devcontainer/                  # Dev container configuration
├── README.md                       # Project overview and instructions
├── requirements.txt                # Python dependencies
├── stock.py                        # Main Streamlit app code
├── stock_data_long_format.csv      # Preprocessed NIFTY 50 dataset
└── stock_prediction_model.h5      # Trained LSTM model file
```

---

## 🧪 How It Works

1. Loads and visualizes historical stock data (`stock_data_long_format.csv`)
2. Preprocesses data for LSTM (windowed time sequences)
3. Loads pre-trained model (`stock_prediction_model.h5`)
4. Predicts future stock prices

---

## 🖥️ Tech Stack

- **Frontend/UI**: Streamlit
- **Data**: yFinance (Yahoo Finance) and preprocessed CSV
- **ML Framework**: TensorFlow (LSTM)
- **Visualization**: Plotly, Matplotlib
- **Languages**: Python, NumPy, Pandas, Scikit-learn

---

## 📦 Installation (for Local Use)

1. Clone the repo:
   ```bash
   git clone https://github.com/stupefyingcoder/Stocksense.git
   cd Stocksense
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run stock.py
   ```

---

## 🧾 Requirements

- Python 3.7+
- See full dependencies in [`requirements.txt`](./requirements.txt)

---

## 📁 Dataset

The dataset (`stock_data_long_format.csv`) contains historical stock prices of multiple NIFTY 50 companies formatted for LSTM-based time series prediction.

---

## 🧠 Model

The model (`stock_prediction_model.h5`) is a trained **LSTM model** for forecasting stock prices based on time-windowed input sequences.

---

## 🙋‍♂️ Author

**Prajwal Prakash Kulkarni**  
AI & Data Science Student  
🔗 [LinkedIn](www.linkedin.com/in/kprajwal206) (optional)  
📧 Email: kprajwal206@gmail.com

---

## 🌟 Show Your Support

If you found this project helpful or interesting:

- ⭐ Star this repo
- 🍴 Fork and experiment
- 📢 Share with others!

---

## 📄 License

This project is under the [MIT License](LICENSE).







