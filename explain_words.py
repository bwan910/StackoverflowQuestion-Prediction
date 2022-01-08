import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import eli5

df2 = pd.read_csv('cleaned_Stackoverflow_data.csv')

X = df2['Body']
y = df2['Tags']

# train data
train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.25,random_state=5,shuffle=True)
vectorizer = TfidfVectorizer(max_df=0.75)
vec_train = vectorizer.fit_transform(train_x)

vec_test = vectorizer.transform(test_x)


clf_log = LogisticRegression()
clf_log.fit(vec_train, train_y)

def explain_words(word):
    

    targetname= ['Java','Javascript','PHP','Python']
    display = eli5.explain_prediction(clf_log, word, vec=vectorizer,target_names=['Java','Javascript','PHP','Python'])

    return display
