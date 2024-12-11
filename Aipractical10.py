import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary resources if not already done
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(sentence)
    lemmatized_sentence = [lemmatizer.lemmatize(word) for word in word_tokens]
    return ' '.join(lemmatized_sentence)

def main():
    sentence = "The striped bats are hanging on their feet for best"
    lemmatized_sentence = lemmatize_sentence(sentence)
    print("Original Sentence:", sentence)
    print("Lemmatized Sentence:", lemmatized_sentence)

if __name__ == "__main__":
    main()
