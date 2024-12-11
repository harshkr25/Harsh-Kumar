import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download punkt tokenizer if not already done
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def stem_sentence(sentence):
    porter = PorterStemmer()
    word_tokens = word_tokenize(sentence)
    stemmed_sentence = [porter.stem(word) for word in word_tokens]
    return ' '.join(stemmed_sentence)

def main():
    sentence = "This is an example sentence to demonstrate the stemming process using NLTK."
    stemmed_sentence = stem_sentence(sentence)
    print("Original Sentence:", sentence)
    print("Stemmed Sentence:", stemmed_sentence)

if __name__ == "__main__":
    main()
