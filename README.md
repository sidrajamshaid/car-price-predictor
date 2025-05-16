# 🚗 Car Price Prediction Project

A machine learning project that predicts used car prices based on data from Craigslist.

### 🔍 Dataset

Source: [Kaggle - Craigslist Car Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)

We use features like:

- year, odometer
- manufacturer, fuel, transmission, drive, car type
- paint color, condition, cylinders

---

### 💡 Model

- Model: Linear Regression (can also switch to Random Forest)
- Preprocessing: OneHotEncoding + StandardScaler
- Pipeline: Scikit-learn
- R² Score: ~0.78
- RMSE: ~5686

---

### 📊 Files

| File                           | Description                          |
| ------------------------------ | ------------------------------------ |
| `car_price_prediction.ipynb` | Main notebook for training the model |
| `car_price_model.pkl`        | Saved ML model                       |
| `app.py`                     | Streamlit app for live predictions   |
| `requirements.txt`           | Python dependencies                  |

---

### 🧪 Try It Locally

```bash
git clone https://github.com/yourusername/car-price-prediction
cd car-price-prediction
pip install -r requirements.txt
streamlit run app.py
```


### 📂 Dataset Not Included

To keep the repo lightweight, `vehicles.csv` is not included.

Please download it from [Kaggle here](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)
and place it in the project folder before running the notebook.
