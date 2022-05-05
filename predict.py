import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_cs
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
import pickle
import json
from  model import df

tfidf_matrix = pickle.load(open('CRS_model.sav', 'rb'))
# Calculating the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#Creating a reverse map of index and course titles
indices = pd.Series(df.index, index=df['Title']).drop_duplicates()

# A function that takes a course title as input and an output course that has some similarities
def get_recommendations(title='none', cosine_sim='none'):
    
    
   
    # Retrieve the index of the entered course
    idx = indices[title.lower()]

    # Take the similarity score of all courses with the input course
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort courses by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    

    # Take the 10 courses that have the highest similarity score
    sim_scores = sim_scores[1:6]

    # Take the course index
    course_indices = [i[0] for i in sim_scores]

    #convert to json
    
    df_return=pd.DataFrame(data=df.iloc[course_indices])
    # Return the top 10 courses that have the highest similarity
    return df_return.to_dict('records')#rec_df.reset_index().to_json(orient='records') #df['Title'].iloc[course_indices]

def fastapi_RSC(title):
    #rec=get_recommendations('HTML and CSS: A Guide to Web Design',cosine_sim)
    rec=get_recommendations(title,cosine_sim)
    #json_object = json.dumps(rec, indent = 4)
    return rec#json_object



	



#print(fastapi_RSC('HTML and CSS: A Guide to Web Design'))
