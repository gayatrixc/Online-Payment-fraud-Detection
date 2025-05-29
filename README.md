# Online Payment Fraud Detection Model

## 🚀 Project Overview
This project aims to build a machine learning model to predict and detect online payment fraud, especially in credit card transactions. With the rapid increase in online payment usage, fraud detection is essential to protect customers from unauthorized charges and financial losses.

## 🎯 Objective
- Detect fraudulent online payment transactions using machine learning.
- Help credit card companies reduce fraud losses and protect customers.
- Achieve high prediction accuracy to ensure reliability.

## 📊 Dataset
- Source: [Kaggle - PaySim1 Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)
- Created by Dr. William H. Wolberg, University of Wisconsin Hospital
- Contains transaction features including:
  - `step`: Time step (1 step = 1 hour)
  - `type`: Transaction type
  - `amount`: Transaction amount
  - `nameOrig`: Customer initiating transaction
  - `oldbalanceOrg`, `newbalanceOrig`: Balance before and after transaction (origin)
  - `nameDest`: Recipient of transaction
  - `oldbalanceDest`, `newbalanceDest`: Recipient’s balance before and after transaction
  - `isFraud`: Fraud label (target variable)

## 🛠️ Tools and Libraries Used
- **Pandas** – Data manipulation and analysis
- **Scikit-learn** – Machine learning algorithms and preprocessing
- **Pickle** – Model serialization and saving
- **Seaborn & Matplotlib** – Data visualization

## 📋 Project Steps

### 1. Import Required Libraries
- Load essential Python libraries for data analysis, visualization, and model building.

### 2. Load and Explore Dataset
- Read dataset into DataFrame.
- Inspect shape, data types, and basic statistics.

### 3. Data Preprocessing
- Handle missing or inconsistent data.
- Drop irrelevant columns.
- Convert categorical data to numeric using Label Encoding.
- Check for null and NaN values.

### 4. Descriptive Analysis
- Analyze distribution and variability of features (mean, median, mode, standard deviation).
- Check data skewness and unique value counts.

### 5. Data Exploration and Visualization
- Plot histograms, pie charts, distplots, heatmaps, and boxplots to understand data relationships.

### 6. Data Preparation
- Separate features and target variable.
- Split data into training and testing sets.
- Scale feature values to improve model performance.

### 7. Model Training
- Train classification models to predict fraud:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Random Forest Classifier
- Evaluate model accuracy and performance.

### 8. Save Model
- Save the best performing model in a Pickle (`.pkl`) file for future use.

### 9. Model Deployment
- Deploy the model via a web API using **Streamlit**.
- Allow users to input transaction data and get fraud predictions through a user-friendly interface.
- Run locally at: `http://localhost:8501`

## 📈 Results
- Achieved **99.77% accuracy** in fraud prediction.
- The model is robust and can effectively detect fraudulent transactions.

## ⚡ How to Run
1. Clone the repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## 🙋‍♀️ Author

**Gayatri**  
🔗 [LinkedIn](https://www.linkedin.com/in/gayatri-xc/)   
📍 Hyderabad, Telangana, India

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
