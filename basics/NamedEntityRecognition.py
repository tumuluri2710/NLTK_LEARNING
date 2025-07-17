import nltk
from cleaning_corpus import corpus_processing
nltk.data.path.append(r'D:\Downloads\NLTK_LEARNING\nltk\Lib\site-packages\nltk_data')
#nltk.download('maxent_ne_chunker_tab')
#nltk.download('words')
#nltk.download('averaged_perceptron_tagger')
class NER(corpus_processing):
    def __init__(self, corpus):
        super().__init__(corpus)
        self.clean_corpus=self.clean_corpus()
        self.named_entities = []

    def extract_named_entities(self):
        tag = nltk.pos_tag(self.clean_corpus.split())
        named_entities = nltk.ne_chunk(tag)
        return named_entities

if __name__ == "__main__":
    text = "Barack Obama was the 44th President of the United States. He was born in Hawaii."
    ne = NER(text)
    named_entities = ne.extract_named_entities()
    print(named_entities)