import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import datetime as dt
import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize

df = pd.read_csv("dataset/udemy_tech.csv")
df['Title']=df['Title'].str.lower()


#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

#Defines a TF-IDF Vectorizer Object. Remove all english stop words like 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Form the required TF-IDF matrix by matching and transforming the data
tfidf_matrix = tfidf.fit_transform(df['Title'])

#Output of tfidf_matrix
import pickle

filename = 'CRS_model.sav'
pickle.dump(tfidf_matrix, open(filename, 'wb'))

