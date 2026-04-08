# 🩺 Breast Cancer Classification with Machine Learning

## 📌 Introduction
Breast cancer is one of the most common cancers worldwide, and early detection is critical for effective treatment.  
This project uses the **Breast Cancer Wisconsin dataset**, a benchmark dataset containing features computed from digitized images of fine needle aspirates of breast masses. Each sample is described by 30 numerical features that capture cell characteristics such as radius, texture, smoothness, and concavity.

The dataset is labeled into two categories:
- **Malignant (cancerous)**
- **Benign (non‑cancerous)**

---

## 🎯 Goal
The primary goal of this project is to build and evaluate machine learning models that can **classify tumors as malignant or benign** based on these features.  
By comparing different models and preprocessing techniques (**Scaled vs PCA**), we aim to identify the most reliable approach for maximizing **recall** — ensuring malignant cases are detected — while maintaining strong overall performance.

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Dropped unnecessary columns (`id`, `Unnamed: 32`)
   - Encoded labels (Malignant = 1, Benign = 0)
   - Standardized features using `StandardScaler`
   - Applied **PCA** for dimensionality reduction and visualization

2. **Exploratory Data Analysis (EDA)**
   - Distribution plots and boxplots for key features
   - Correlation heatmaps to identify highly predictive features
   - PCA scatterplots to visualize separation between classes

3. **Modeling**
   - Models used: Logistic Regression, Random Forest, XGBoost, SVM, KNN
   - Evaluated on both **Scaled** and **PCA-transformed** data
   - Metrics: Accuracy, Precision, Recall, F1, ROC-AUC

4. **Visualization**
   - Confusion matrices
   - ROC curves (Scaled vs PCA)
   - Bar charts comparing Accuracy and F1 across models

---

## 📊 Results
- **Logistic Regression with PCA** achieved the best overall performance:
  - Accuracy ≈ 99%
  - F1 ≈ 0.99
  - ROC-AUC ≈ 0.99
- Confusion matrix showed **one malignant case misclassified as benign (false negative)**.
- Recall remained very high, but this highlights the importance of minimizing false negatives in medical contexts.

---

## 🏁 Conclusion
Logistic Regression with PCA is a strong and reliable model for breast cancer classification.  
Although one malignant case was missed, recall remains high, and overall performance is excellent.  
In medical applications, **recall is the most critical metric** — false negatives are dangerous, while false positives only lead to additional testing.  

**Key Takeaway:**  
👉 Logistic Regression with PCA provides high accuracy and sensitivity, making it a safe choice for detecting malignant cases, with threshold tuning as a possible improvement to further reduce false negatives.

---

## 📂 Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Plotly)
- **Machine Learning Models**: Logistic Regression, Random Forest, XGBoost, SVM, KNN
- **Preprocessing**: StandardScaler, PCA
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1, ROC-AUC
