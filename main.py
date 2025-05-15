# ✅ Step 1: Install and import necessary libraries
# !pip install scikit-learn matplotlib pandas numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ✅ Step 2: Load and clean the dataset
df = pd.read_csv('vehicles.csv')

# Select relevant features including high-impact ones
df = df[['price', 'year', 'odometer', 'manufacturer', 'fuel',
         'transmission', 'drive', 'type', 'paint_color', 'condition', 'cylinders']]

# Drop missing values
df = df.dropna()

# Remove outliers and unrealistic entries
df = df[(df['price'] > 1000) & (df['price'] < 60000)]
df = df[(df['odometer'] < 300000) & (df['year'] > 1990)]

# Reset index
df.reset_index(drop=True, inplace=True)

# Optional: visualize price distribution
df['price'].hist(bins=50, figsize=(8, 5))
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# ✅ Step 3: Define features and target
X = df.drop(columns='price')
y = df['price']

# ✅ Step 4: Specify column types
categorical_cols = ['manufacturer', 'fuel', 'transmission', 'drive',
                    'type', 'paint_color', 'condition', 'cylinders']
numeric_cols = ['year', 'odometer']

# ✅ Step 5: Create preprocessing pipeline
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numeric_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# ✅ Step 6: Define and build the model pipeline
# You can swap LinearRegression() with RandomForestRegressor() if needed
regressor = LinearRegression()
# regressor = RandomForestRegressor(n_estimators=100, random_state=42)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', regressor)
])

# ✅ Step 7: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Step 8: Train the model
model.fit(X_train, y_train)

# ✅ Step 9: Evaluate the model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"✅ RMSE: {rmse:.2f}")
print(f"✅ R² Score: {r2:.2f}")