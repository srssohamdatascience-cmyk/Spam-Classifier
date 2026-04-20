import re
import string

def clean_text(text):
    text = str(text).lower()
    
    # 🔹 Remove email headers (robust: works with or without newline)
    text = re.sub(r'\b(subject|from|to|cc)\b\s*:?\s*', '', text)
    
    # 🔹 Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # 🔹 Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 🔹 Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text