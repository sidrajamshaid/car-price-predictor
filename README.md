# 🚗 Car Price Predictor Using Linear Regression & Random Forest

A sleek, interactive **machine learning web app** that estimates used car prices based on details like year, mileage, brand, and condition — all in real time 🧠💸

Built with:

- 🧪 **Scikit-learn** for model building
- 🌲 **Random Forest** for improved predictions
- 🎨 **Streamlit** for a user-friendly interface
- 🚀 **Hugging Face Spaces** for public deployment

---

## 💡 How the Model Was Built (AI Work)

Here’s a breakdown of what I did in the project 👇

### 📦 1. Data Preparation

- Cleaned and filtered the **Craigslist car dataset**
- Removed noisy data and handled null/missing values
- Selected meaningful features:
  - `year`, `odometer`, `manufacturer`, `fuel`, `transmission`, `condition`, `cylinders`, etc.

### 🧠 2. Model Pipeline

- Encoded categorical variables using `OneHotEncoder`
- Scaled numerical features using `StandardScaler`
- Combined preprocessing and **Linear Regression** into a single pipeline using `Pipeline`

### 📈 3. Training & Evaluation

- Trained on real-world used car data
- Model Performance (Linear Regression):
  - 📊 **R² Score** ≈ 0.73
  - 📉 **RMSE** ≈ 6130
- Exported trained pipeline as `car_price_model.pkl` using `joblib`

### 🖥️ 4. App Integration & Deployment

- Developed a fully functional Streamlit app for live predictions
- Styled the UI with custom CSS
- Connected the model to Hugging Face Spaces for easy access
  👉 [🚀 Live App](https://huggingface.co/spaces/Sidrajamshaid/car-price-predictor)

---

## 🧰 Technologies Used

| Tool            | Purpose                        |
| --------------- | ------------------------------ |
| 🐍 Python       | Core programming language      |
| 📊 Pandas       | Data cleaning & manipulation   |
| 🧪 Scikit-learn | Preprocessing + model pipeline |
| 🌲 RandomForest | Alternative ML model           |
| 📦 Joblib       | Saving/loading trained model   |
| 🎨 Streamlit    | Web app interface              |
| 🚀 Hugging Face | Public deployment (Spaces)     |

---

## 📁 Project Structure

| File                                            | Description                      |
| ----------------------------------------------- | -------------------------------- |
| `app.py`                                      | Streamlit app script             |
| `car_price_model.pkl`                         | Trained model pipeline           |
| `requirements.txt`                            | Dependencies for running the app |
| `style.css`                                   | Optional: Custom UI styling      |
| `space.yaml`                                  | Hugging Face Space config        |
| `Car_price_modelling_and_prediction.ipynb`    | Linear Regression model notebook |
| `Car_price_modelling_and_prediction_RF.ipynb` | Random Forest + EDA notebook     |

---

### 🔍 Additional Model Insights (Linear Regression)

- **Features engineered:** One-hot encoding for categorical variables, standardization for `year` and `odometer`.
- **Training performance (Linear Regression):**
  - **R² Score:** ~0.73
  - **RMSE:** ~6130
- **EDA findings:**
  - Outliers removed using IQR method.
  - Features like `drive`, `fuel`, `condition`, and `cylinders` have major influence on price.
- **Bonus:** Neural Network and Random Forest were also tested.

---

### 🌲 Random Forest Regressor Model

- **Training performance (Random Forest):**
  - **R² Score:** ~0.88
  - **RMSE:** ~4234
- **Visuals included:** Actual vs Predicted Price, Residual distribution.
- **Inference:** RF gave significantly better results than LR, capturing non-linear relationships.

---

## 🔧 Run Locally in 3 Easy Steps

```bash
git clone https://github.com/sidrajamshaid/car-price-predictor
cd car-price-predictor
pip install -r requirements.txt
streamlit run app.py
```


### **📉 Dataset Note**

> ⚠️ **Note:** The dataset file **vehicles.csv** is **not included** in this repository because it exceeds GitHub’s file size limit (100 MB).

> To retrain the model or explore the data:

* **🔗 Download it from **[**Kaggle - Craigslist Car Listings**](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)
* 📂 Save the file as **vehicles.csv** in the project’s **root directory**
* 🛠️ Then you can rerun the notebook or retrain the model
