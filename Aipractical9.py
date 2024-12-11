import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download necessary resources if not already done
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(sentence):
    word_tokens = word_tokenize(sentence)
    pos_tags = pos_tag(word_tokens)
    return pos_tags

def main():
    sentence = "This is an example sentence to demonstrate POS tagging using NLTK."
    pos_tags = pos_tagging(sentence)
    print("Original Sentence:", sentence)
    print("POS Tags:", pos_tags)

if __name__ == "__main__":
    main()
