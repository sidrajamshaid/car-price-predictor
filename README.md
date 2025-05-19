# 🚗 Car Price Predictor Using Linear Regression

A sleek, interactive **machine learning web app** that estimates used car prices based on details like year, mileage, brand, and condition — all in real time 🧠💸

Built with:

- 🧪 **Scikit-learn** for model building
- 🎨 **Streamlit** for a user-friendly interface
- 🚀 **Hugging Face Spaces** for public deployment

---

## 💡 How the Model Was Built (My AI Work)

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
- Model Performance:
  - 📊 **R² Score** ≈ 0.78
  - 📉 **RMSE** ≈ 5686
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
| 📦 Joblib       | Saving/loading trained model   |
| 🎨 Streamlit    | Web app interface              |
| 🚀 Hugging Face | Public deployment (Spaces)     |

---

## 📁 Project Structure

| File                    | Description                      |
| ----------------------- | -------------------------------- |
| `app.py`              | Streamlit app script             |
| `car_price_model.pkl` | Trained model pipeline           |
| `requirements.txt`    | Dependencies for running the app |
| `style.css`           | Optional: Custom UI styling      |
| `space.yaml`          | Hugging Face Space config        |

---

## 🔧 Run Locally in 3 Easy Steps

```bash
git clone https://github.com/sidrajamshaid/car-price-predictor
cd car-price-predictor
pip install -r requirements.txt
streamlit run app.py
```
