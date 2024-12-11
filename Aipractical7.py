import nltk  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.tokenize import word_tokenize  # type: ignore

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(text):
    """
    Removes stopwords from the given text using NLTK.

    Args:
        text (str): Input text from which stopwords need to be removed.

    Returns:
        str: Text after removing stopwords.
    """
    stop_words = set(stopwords.words('english'))  # Get the set of stopwords
    word_tokens = word_tokenize(text)  # Tokenize the text into words
    # Filter out the stopwords
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)  # Join the filtered words into a single string

def main():
    """
    Reads a text passage from 'input.txt', removes stopwords, 
    and writes the filtered text to 'output.txt'.
    """
    try:
        # Read input from a file
        with open('input.txt', 'r') as file:
            text = file.read()

        # Remove stopwords
        filtered_text = remove_stopwords(text)

        # Write the filtered text to a new file
        with open('output.txt', 'w') as file:
            file.write(filtered_text)

        print("Stopwords removed successfully. Check 'output.txt' for the result.")
    
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please ensure the file exists in the same directory.")

if __name__ == "__main__":
    main()
