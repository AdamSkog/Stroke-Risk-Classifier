# Stroke Prediction Model
This repository contains the code and resources used to build a Stroke Prediction model and deploy it as a Streamlit web application. The model predicts the risk of stroke based on medical and demographic information provided by users.

Streamlit App Link: [Stroke Prediction App](https://strokerisk.streamlit.app/)

Overview
The Stroke Prediction model was developed using Python and various machine learning libraries. The following sections provide an overview of the steps taken to create the model:

1. Data Collection
The dataset used for this project was obtained from [kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). It contains a collection of medical and demographic data points, including age, hypertension, heart disease, glucose levels, BMI, gender, marital status, employment type, residency, and smoking status. This dataset served as the foundation for training and evaluating the model.

2. Exploratory Data Analysis (EDA)
Before building the model, exploratory data analysis (EDA) was conducted to gain insights into the dataset. This involved:

Visualizing data distributions.
Identifying missing values.
Analyzing correlations between features.
Exploring the balance of the target variable (stroke/no-stroke).

3. Data Cleaning
To prepare the data for modeling, essential data cleaning steps were performed:

Handling missing values by imputation or removal.
Encoding categorical variables for machine learning compatibility (e.g., one-hot encoding).

4. Preprocessing
Data preprocessing was a crucial step to ensure the data was ready for machine learning. This included:

Scaling numeric features to a standard range.
Handling class imbalance through oversampling or undersampling techniques.
Preparing the data for model input.

5. Model Selection
Choosing the right machine learning algorithm is essential. Several models were evaluated, including Logistic Regression and XGBoost. The model that demonstrated the best performance in terms of accuracy and other relevant metrics was selected as the final model.

6. Pipeline Creation
A machine learning pipeline was constructed to streamline the entire process from data preprocessing to model training. This pipeline included:

Data preprocessing steps.
Feature scaling.
Model training and evaluation.

7. Streamlit App Deployment
The selected model was deployed as a Streamlit web application. Users can input their medical and demographic information, and the app provides a real-time prediction of stroke risk. The app's user interface was designed to be intuitive and user-friendly.

Notice
It's important to note that the Stroke Prediction model has limitations:

The model's performance may be affected by the imbalance in the dataset. It is more likely to classify individuals as not at risk of stroke due to the dataset's class distribution.
The model's predictions should not be considered a definitive diagnosis. They are intended for informational purposes only.

Feedback and Contributions
Contributions and feedback are welcome. If you would like to contribute to the improvement of the model or the app, please feel free to do so.
