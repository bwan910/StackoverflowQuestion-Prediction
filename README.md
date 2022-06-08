# StackoverflowQuestion-Prediction: Project Overview
<p>Created a tool that predicts tags for Stackoverflow questions for (Java, Javascript, PHP, Python only). Built a web interface using Streamlit for testing the model. <p>


## Resources used
Python Version: 3.8.7

Data can be obtained from this database with SQL queries: <https://data.stackexchange.com/stackoverflow/query/edit/1186275>

Libraries used in model training: pandas, matplotlib, nltk, re, string, sklearn, seaborn, yellowbrick, eli5, pickle.

Libraries for web app: streamlit, requests, joblib, pickle, os
  
## File structure:

1) File for the trained model: Model_Train.ipynb: 
2) File for the Web interface: To run the application type command: *streamlit run app.py*
3) Original dataset file: All_data.csv
4) Cleaned dataset file: cleaned_Stackoverflow_data.csv
5) Necessary files to run the web app are in Pickle_file folder. 

## Methodology for Training with Machine Learning
1) Data Collection: <https://data.stackexchange.com/stackoverflow/query/edit/1186275>
2) Exploratory Data Analysis were performed to explore dataset
3) Data Preprocessing
4) Train Test Split data, Ratio of 80% train and 20% test
5) Optimized few Machine Learning Algorithms: Decision Tree, Logistic Regression and Multinomial Naive Bayes to reach the best model.
6) Model evaluated with a few metrics (Accuracy, Precision, Recall, ROCAUC)
7) Created Model explainer(Text Feature explanation) with ELI5 

## Methodology for Training with Deep Learning (Transformer-Bert)
  
1) Using the cleaned dataset file: cleaned_Stackoverflow_data.csv.
2) Convert Tag column into Categorical Data as Integer representation.
3) Train Test Split, Ratio of 80% train and 20% test.
4) Converting our integer coded Tag column into categorical data(matrix)
5) Input Data Modeling before training, convert the input textual data into BERT’s input data format using a tokenizer.
6) After data modelling, the tokenizer will return a dictionary (x_train) containing ‘Input_ids’, ‘attention_mask’ as key for their respective data.
7) Model Building
8) Model Evaluation


## Model Findings
#### Accuracy:
|        Algorithms       | Accuracy |
|:-----------------------:|:--------:|
|   Logistic Regression   |    92%   |
| Multinomial Naive Bayes |    88%   |
|      Decision Tree      |    87%   |
|  Transformers-Bert      |    90%   |

### Classfication Report for model training with Transformer Bert
<img width="432" alt="image" src="https://user-images.githubusercontent.com/45889977/172563006-7b620f37-2044-4423-85c7-6df1ae553d2a.png">


  
#### ROCAUC curve:
![ROCAUC Curve](https://user-images.githubusercontent.com/45889977/148638390-49714172-fa79-4517-8afe-27d33809693b.JPG)

#### Feature texts contributions:
<img width="521" alt="Screenshot 2022-01-08 at 5 02 04 PM" src="https://user-images.githubusercontent.com/45889977/148638539-2a30b862-ca2f-4279-8e08-dc087a2f6e74.png">


