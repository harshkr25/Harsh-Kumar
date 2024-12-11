import string
text = "Hello, world! Welcome to Python."
result = text.translate(str.maketrans('', '', string.punctuation))
print(result)