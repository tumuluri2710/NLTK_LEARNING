
import nltk
import  pandas as pd
import re
from nltk.tokenize import  sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import  CountVectorizer
nltk.data.path.append(r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')
data=pd.read_csv('review.csv',sep='\t',names=['product_name','review_text'])
stopwords=stopwords.words('english')
corpus=[]
lemmatizer=WordNetLemmatizer()
for i in range(0,len(data)):
    review=data['review_text'][i]
    review=re.sub(',','',review)
    review=" ".join(review.strip().split())
    review=review.replace('.','')
    review=review.lower()
    review=wordpunct_tokenize(review)
    review=[lemmatizer.lemmatize(word) for word in review if word  not in stopwords]
    corpus.append(review)
#print(corpus)
vector=CountVectorizer()
for i in corpus:
    vec=vector.fit_transform(i).toarray()
    print(vector.get_feature_names_out())




