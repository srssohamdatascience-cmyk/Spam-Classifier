from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import nltk

class TextStats(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        features = []
        for text in X:
            num_words = len(text.split())
            num_chars = len(text)
            num_sentences = len(nltk.sent_tokenize(text))
            avg_word_length = num_chars / num_words if num_words != 0 else 0
            
            features.append([num_words, num_chars, num_sentences, avg_word_length])
        
        return np.array(features)