# 📊 Customer Churn Prediction

## 🚀 Project Overview

This project focuses on analyzing customer behavior and predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave and provide actionable insights to improve customer retention.

---

## 🎯 Objectives

* Analyze customer data to identify churn patterns
* Perform data preprocessing and exploratory data analysis (EDA)
* Build and evaluate machine learning models
* Segment customers based on risk factors
* Provide business recommendations to reduce churn

---



---

## 🧹 Data Preprocessing

* Handled missing values and empty spaces
* Converted data types (e.g., TotalCharges to numeric)
* Removed duplicates
* Created new features such as tenure groups

---

## 📊 Exploratory Data Analysis (EDA)

Key insights:

* Customers with **month-to-month contracts** have higher churn
* Customers with **short tenure (0–12 months)** are more likely to churn
* Higher **monthly charges** are associated with increased churn
* Certain **payment methods** show higher churn behavior

---

## 📈 Customer Segmentation

Customers were segmented based on:

* Tenure groups
* Monthly charges
* Contract type

This helped identify **high-risk customer groups** for targeted retention strategies.

---

## 🤖 Model Building

### Models Used:

* Logistic Regression (with class balancing & scaling)
* Random Forest Classifier

### Final Model Selected:

✅ **Random Forest Classifier (Balanced + Scaled)**

---

## 📊 Model Performance

| Metric               | Logistic Regression | Random Forest |
| -------------------- | ------------------- | ------------- |
| Accuracy             | 0.74                | 0.79          |
| Recall (Churn = Yes) | 0.80                | 0.48          |
| F1 Score             | 0.62                | 0.54          |

👉 Logistic Regression was selected because it **better identifies churn customers**, which is critical for business.

---

## 🔍 Key Insights from Model

* Short tenure customers are more likely to churn
* High monthly charges increase churn probability
* Contract type significantly impacts churn behavior

---

## 💡 Business Recommendations

* Improve onboarding for new customers
* Encourage long-term contracts with incentives
* Optimize pricing strategies
* Use predictive model to target high-risk customers
* Enhance customer experience and support

---

## 📌 Tools & Technologies

* Python
* Pandas, NumPy
* Seaborn, Matplotlib
* Scikit-learn




## 🧠 Conclusion

This project demonstrates an end-to-end machine learning workflow, from data preprocessing to model deployment. The insights and predictive model can help businesses reduce churn and improve customer retention strategies.

---
