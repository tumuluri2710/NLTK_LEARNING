import nltk
nltk.download('wordnet',download_dir=r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')

nltk.data.path.append(r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')   
from nltk.stem import WordNetLemmatizer
def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word, pos='v')  # 'n' for noun, can be changed to 'v' for verb, etc.
if __name__ == "__main__":
    word = "running"
    print("Lemmatized Word:", lemmatize_word(word))
    word = "happily"
    print("Lemmatized Word:", lemmatize_word(word))
    word = "goes"
    print("Lemmatized Word:", lemmatize_word(word))
    word = "better"
    print("Lemmatized Word:", lemmatize_word(word))