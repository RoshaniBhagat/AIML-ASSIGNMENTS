'''Assignment (21/03/2026) 
Assignment Name : Build a Text Cleaner 
Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.'''

#RUN IN JUPYTER NOTEBOOK OR PYTHON ENVIRONMENT WITH NLTK INSTALLED
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
   
    text = text.lower()

  
    text = text.translate(str.maketrans('', '', string.punctuation))

   
    words = word_tokenize(text)

    
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


sample_text = "Hello!!! This is a simple TEXT cleaning example."

print("Original:", sample_text)
print("Cleaned :", clean_text(sample_text))


#OUTPUT:
'''Original: Hello!!! This is a simple TEXT cleaning example.
Cleaned : hello simple text cleaning example'''