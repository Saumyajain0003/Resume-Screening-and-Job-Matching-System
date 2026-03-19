import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure stopwords and wordnet are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    """
    Cleans raw text for NLP processing.
    1. Converts to lowercase.
    2. Removes special characters, numbers, and punctuation.
    3. Removes standard English stopwords.
    """
    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove special characters except the ones used in tech (like C++, C#, .NET)
    # Replaces everything else with space to maintain word separation
    text = re.sub(r'[^a-zA-Z0-9\s\+\#\.-]', ' ', text)

    # Tokenize (splitting by whitespace)
    words = text.split()

    # Remove stopwords and apply lemmatization
    stop_words = set(stopwords.words('english'))
    cleaned_words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]

    # Join back into a single string
    return " ".join(cleaned_words)

if __name__ == "__main__":
    # Quick manual test
    sample_text = "I am a Python Developer with 5 years of experience! Learning NLP is great."
    print(f"Original: {sample_text}")
    print(f"Cleaned: {clean_text(sample_text)}")
