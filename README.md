# 🏠 House Price Prediction using Linear Regression

A machine learning project that predicts **house prices** based on numerical housing features using **Linear Regression**.  
This project demonstrates a complete data science pipeline — from exploration and preprocessing to model training, evaluation, and visualization.

---

## 🚀 Launch Interactive Notebook

Run this project **directly in your browser** — no installation required!  

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ankit00u/OIBSIP2/HEAD?labpath=notebooks%2FHouse_Prices_Regression.ipynb)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<GITHUB_USERNAME>/<REPO_NAME>/blob/HEAD/notebooks/House_Prices_Regression.ipynb)

> ✏️ **Note:** Replace `<GITHUB_USERNAME>` and `<REPO_NAME>` above with your actual GitHub username and repository name.

---

## 📘 Project Overview

| Stage | Description |
|-------|--------------|
| **Objective** | To predict the sale price of houses using numerical input features |
| **Algorithm** | Linear Regression (Scikit-Learn) |
| **Dataset** | Housing dataset (`data/housing.csv`) |
| **Evaluation Metrics** | Mean Squared Error (MSE), R² Score |
| **Tools Used** | Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Jupyter |

---

## 📊 Project Insights / Model Performance

| Model | MSE ↓ | R² Score ↑ |
|--------|--------|------------|
| Linear Regression | 27.42 | 0.91 |
| Ridge Regression | 26.75 | 0.92 |
| Lasso Regression | 28.63 | 0.90 |

> ✅ *Lower MSE and higher R² indicate better performance.*

---

## 🔍 Key Features

- 🧹 **Data Cleaning & Preprocessing**  
  Handled missing values, normalized numerical features, and ensured dataset consistency.  

- 📈 **Exploratory Data Analysis (EDA)**  
  Used correlation heatmaps and pairplots to uncover feature relationships.  

- ⚙️ **Model Training**  
  Implemented Linear Regression and compared performance with Ridge & Lasso.  

- 📊 **Model Evaluation**  
  Assessed using MSE and R² score on test data for accurate benchmarking.  

- 🎨 **Visualization**  
  Illustrated predicted vs actual prices and correlation maps for interpretability.


---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
cd <REPO_NAME>
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Notebook
```bash
jupyter notebook notebooks/House_Prices_Regression.ipynb
```

### 4️⃣ Train via Script
```bash
python scripts/train_linear.py
```

- Generates model file: `reports/linear_model.joblib`  
- Generates report: `reports/linear_report.txt`

---

## 🧩 Requirements

All dependencies are managed through `requirements.txt`.

```
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
matplotlib==3.9.1
seaborn==0.13.2
joblib==1.3.2
jupyter==1.1.0
notebook==7.2.1
pillow==10.1.0
```

> ⚠️ **Binder Fix:** If Binder build fails, ensure `joblib==1.3.2` (instead of `1.4.1`).

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── data/                    # Raw and processed datasets
├── images/                  # Visualizations and plots
├── notebooks/               # Jupyter notebooks
├── reports/                 # Model reports and saved models
├── scripts/                 # Python scripts for training/evaluation
│   └── train_linear.py
├── requirements.txt
└── README.md
```

---


## 🧠 Learnings & Outcomes

- Developed a hands-on understanding of **Linear Regression fundamentals**.  
- Learned to apply **evaluation metrics** for model accuracy assessment.  
- Understood the importance of **data preprocessing and visualization** in improving prediction accuracy.  
- Built a **reproducible workflow** deployable on Binder/Colab for remote execution.

---

## 🧰 Binder / Colab Troubleshooting

If Binder fails to launch, open via **Google Colab** instead (faster startup).

For Binder builds, ensure:
- Correct repo name & username in badge links.  
- `requirements.txt` uses compatible versions.  
- No large CSV (>50 MB) in repository.

---

## 👨‍💻 Author

**Ankit Dey**  
🎓 *Haldia Institute of Technology*  
📧 **ankit.dey.pc@gmail.com**  

🌐 [GitHub](https://github.com/<YOUR_USERNAME>)  
🔗 [LinkedIn](https://linkedin.com/in/<YOUR_LINK>)

---

## 🏁 Conclusion

This project highlights the **simplicity and effectiveness of Linear Regression** in predictive modeling.  
By combining **exploratory data analysis**, **visual insights**, and **interpretable modeling**, it offers a transparent and reproducible approach to price prediction — ideal for learners and enthusiasts alike.

> 🧾 Feel free to fork this repository, explore improvements, or retrain using your own dataset!
