"""Train a simple Linear Regression model on housing data and save evaluation report.
Usage: python scripts/train_linear.py
"""
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

data_path = Path(__file__).resolve().parents[1] / 'data' / 'housing.csv'
df = pd.read_csv(data_path)

possible_targets = [c for c in df.columns if 'price' in c.lower() or 'sale' in c.lower()]
target_col = possible_targets[0] if possible_targets else df.columns[-1]
print('Using target column:', target_col)

X = df.drop(columns=[target_col])
y = df[target_col]

X_num = X.select_dtypes(include=['number']).fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X_num, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)
preds = lr.predict(X_test)

mse = mean_squared_error(y_test, preds)
r2 = r2_score(y_test, preds)

reports_dir = Path(__file__).resolve().parents[1] / 'reports'
reports_dir.mkdir(exist_ok=True)
with open(reports_dir / 'linear_report.txt', 'w') as f:
    f.write(f'MSE: {mse}\nR2: {r2}\n')

joblib.dump(lr, reports_dir / 'linear_model.joblib')
print('Training complete. Reports and model saved to reports/')