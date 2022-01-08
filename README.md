# StackoverflowQuestion-Prediction: Project Overview

## File structure:

1) File for the trained model: Model_Train.ipynb: 
2) File for the Web interface: To run the application type command: *streamlit run app.py*
3) Original dataset file: All_data.csv
4) Cleaned dataset file: cleaned_Stackoverflow_data.csv
5) Necessary files to run the web app are in Pickle_file folder. 

## Methodology
- Created a tool that predicts tags for Stackoverflow questions for (Java, Javascript, PHP, Python only).
- Exploratory Data Analysis were performed to explore dataset
- Data Preprocessing
- Optimized Decision Tree, Logistic Regression and Multinomial Naive Bayes to reach the best model.
- Model evaluated with a few metrics (Accuracy, Precision, Recall and etc)
- Built a web interface using Streamlit

## Resources used
Python Version: 3.8.7

Data can be obtained from this database with SQL queries: <https://data.stackexchange.com/stackoverflow/query/edit/1186275>

Libraries used in model training: pandas, matplotlib, nltk, re, string, sklearn, seaborn, yellowbrick, eli5, pickle.

Libraries for web app: streamlit, requests, joblib, pickle, os
