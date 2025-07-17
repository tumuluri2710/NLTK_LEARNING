
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.data.path.append(r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')  # Adjust the path as necessary

class corpus_processing:
    def __init__(self,corpus):
        self.corpus = corpus
    def clean_corpus(self):
        sentences = sent_tokenize(self.corpus)
        words=word_tokenize(self.corpus)
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))    
        cleaned_sentences = []
        for sentence in sentences:  
            words = word_tokenize(sentence)
            words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
            cleaned_sentences.append(' '.join(words))   
        cleaned_corpus = ' '.join(cleaned_sentences)
        return cleaned_corpus

#print(cleaned_corpus)
if __name__ == "__main__":
    processing = corpus_processing("""The quick brown fox jumps over the lazy dog. The dog barked back.""")
    cleaned_corpus = processing.clean_corpus()