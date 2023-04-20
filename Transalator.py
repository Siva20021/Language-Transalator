import nltk
from googletrans import Translator

# Set up NLTK for tokenization
nltk.download('punkt')

# Initialize translator object
translator = Translator()

# Get input text from user
input_text = input("Enter some text: ")

# Detect the input text's language
detected_lang = translator.detect(input_text).lang

# Translate the input text to Spanish
translated = translator.translate(input_text, dest="ta")

# Print the results
print("Original text ({}): {}".format(detected_lang, input_text))
print("Translated text (ta): {}".format(translated.text))
