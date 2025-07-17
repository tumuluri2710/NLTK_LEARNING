import nltk

from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer   
from nltk.stem import SnowballStemmer 
def stem_word(word):
    porter_stem=PorterStemmer()
    return porter_stem.stem(word)
def regexp_stem_word(word):
    regexp_stem=RegexpStemmer(r'(?i)(ing|ed|es|s)$')
    return regexp_stem.stem(word)
def Snowball_stem_word(word):
    snowball_stem=SnowballStemmer("english")
    return snowball_stem.stem(word)
if __name__ == "__main__":
    word = "running"
    print("Porter Stemmer:", stem_word(word))
    print("Regexp Stemmer:", regexp_stem_word(word))
    print("Snowball Stemmer:", Snowball_stem_word(word))
    word = "happily"
    print("Porter Stemmer:", stem_word(word))
    print("Regexp Stemmer:", regexp_stem_word(word))
    print("Snowball Stemmer:", Snowball_stem_word(word))
    word ="goes"
    print("Porter Stemmer:", stem_word(word))
    print("Regexp Stemmer:", regexp_stem_word(word))
    print("Snowball Stemmer:", Snowball_stem_word(word))

