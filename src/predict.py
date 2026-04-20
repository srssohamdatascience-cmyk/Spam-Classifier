import sys
import os
import pickle
import pandas as pd
import nltk
nltk.download('punkt')
# Fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text
from src.features import TextStats   # ⭐ REQUIRED

# Load model
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(BASE_DIR, 'model', 'pipeline.pkl')

pipeline = pickle.load(open(model_path, 'rb'))

def predict_message(text):
    cleaned = clean_text(text)
    
    df = pd.DataFrame({
        'cleaned_text': [cleaned]
    })
    
    pred = pipeline.predict(df)[0]
    
    return "Spam" if pred == 1 else "Ham"


