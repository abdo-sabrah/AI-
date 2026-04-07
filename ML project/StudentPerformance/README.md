# Student Performance Analysis Project

## 📌 Overview
This project analyzes factors influencing student exam performance using the **StudentPerformanceFactors.csv** dataset. It applies data preprocessing, exploratory data analysis (EDA), feature engineering, and machine learning models to predict exam scores.

---

## 📂 Dataset
- **Rows:** 6607  
- **Columns:** 20 (numeric + categorical)  
- **Target:** `Exam_Score`

### Key Features
- **Numeric:** Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Tutoring_Sessions, Physical_Activity  
- **Categorical:** Parental_Involvement, Access_to_Resources, Extracurricular_Activities, Motivation_Level, Internet_Access, Family_Income, Teacher_Quality, School_Type, Peer_Influence, Learning_Disabilities, Parental_Education_Level, Distance_from_Home, Gender  

---

## 🛠️ Preprocessing
- **Missing Values:** Imputed with most frequent values for categorical features (Teacher_Quality, Parental_Education_Level, Distance_from_Home).  
- **Scaling:** StandardScaler applied to numeric features.  
- **Encoding:** OneHotEncoder applied to categorical features.  
- **Outlier Handling:** Outliers in Tutoring_Sessions retained (valid real-world patterns).  

---

## 📊 Exploratory Data Analysis (EDA)
- **Exam Score Distribution:** Mean ~67, Std ~3.9.  
- **Top Correlations with Exam Score:**  
  - Attendance (r = 0.58)  
  - Hours_Studied (r = 0.45)  
  - Previous_Scores (r = 0.18)  
  - Tutoring_Sessions (r = 0.16)  

- **Categorical Insights:**  
  - Higher parental involvement, family income, and access to resources → higher exam scores.  
  - Postgraduate parental education → highest average scores.  

---

## 🤖 Modeling
Two models were trained and compared:

### 1. Linear Regression
- **MAE:** 0.45  
- **RMSE:** 1.80  
- **R²:** 0.77 (77% variance explained)  

### 2. Random Forest Regressor
- **MAE:** 1.18  
- **RMSE:** 2.23  
- **R²:** 0.65 (65% variance explained)  

**Result:** Linear Regression outperformed Random Forest for this dataset.

---

## 📈 Visualizations
- Histograms and boxplots for exam scores.  
- Scatterplots with regression lines for numeric features vs exam score.  
- Boxplots for categorical features vs exam score.  
- Correlation heatmap of numeric features.  
- Residual plots comparing Linear Regression and Random Forest.  

---

## ✅ Conclusions
- Attendance and study hours are the strongest predictors of exam performance.  
- Socioeconomic and parental factors also influence outcomes.  
- Linear Regression provided better predictive accuracy than Random Forest.  
- Outliers in tutoring sessions represent genuine high-achieving students and should be retained.  

---

## 🚀 Next Steps
- Try advanced models (XGBoost, Gradient Boosting).  
- Perform feature selection using mutual information.  
- Explore interaction features (e.g., Attendance × Hours_Studied).  
- Deploy pipeline for automated predictions.  

---

## 📎 Requirements
- Python 3.x  
- Libraries: numpy, pandas, matplotlib, seaborn, scikit-learn  

---

## 👨‍💻 Author
Prepared by Abdo for applied machine learning and data science practice.
