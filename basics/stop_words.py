import nltk
#nltk.download('stopwords',download_dir=r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')
nltk.data.path.append(r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data') 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
#print("Stop Words in English:", stop_words)
paragraph = """
The quick brown fox jumps over the lazy dog. She was running faster than anyone else in the race. 
Children are playing happily in the garden, enjoying the fresh air and sunshine. 
He studies hard to achieve his goals and dreams of becoming a scientist one day. 
They were talking and laughing together, sharing stories from their childhood. 
Birds are flying high in the sky, singing beautiful songs every morning. 
The leaves are falling from the trees, covering the ground with a colorful carpet. 
He enjoys reading interesting books and often visits the library after school. 
The cats were chasing the mice all night, making a lot of noise in the kitchen. 
We are planning to visit the museum tomorrow to learn about ancient civilizations. 
Everyone is excited about the upcoming festival and preparing delicious food at home.
"""
from nltk.tokenize import  sent_tokenize, word_tokenize
# Tokenizing the paragraph into sentences
sentences = sent_tokenize(paragraph)            
# Tokenizing the paragraph into words
words = word_tokenize(paragraph)   

from nltk.stem import PorterStemmer
porter= PorterStemmer()
port_stemmed_words = [porter.stem(word) for word in words if word.lower() not in stop_words]
for i in port_stemmed_words:
    print(i, end=' ')
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer("english")
snowball_stemmed_words = [snowball.stem(word) for word in words if word.lower() not in stop_words]
print("\nSnowball Stemmed Words:")
for i in snowball_stemmed_words:    
    print(i, end=' ')       
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words if word.lower() not in stop_words]
print("\nLemmatized Words:")    
for i in lemmatized_words:
    print(i, end=' ')