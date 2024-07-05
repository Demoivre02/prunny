import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


df = pd.DataFrame({
    'Reviews': [
        "This product is amazing! I love it.",
        "Not very good. Disappointed with the quality.",
        "Average product, nothing special.",
        "Terrible experience. Would not recommend."
    ]
})


def simple_sentiment(text):
    positive_words = ['amazing', 'love', 'good', 'great', 'excellent']
    negative_words = ['bad', 'terrible', 'disappointed', 'poor', 'not']
    
    words = text.lower().split()
    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)
    
    return (positive_count - negative_count) / (positive_count + negative_count + 1)  


df['Sentiment'] = df['Reviews'].apply(simple_sentiment)


df['ReviewLength'] = df['Reviews'].apply(len)


vectorizer = CountVectorizer(stop_words='english', max_features=10)
word_count_matrix = vectorizer.fit_transform(df['Reviews'])
word_count_df = pd.DataFrame(word_count_matrix.toarray(), columns=vectorizer.get_feature_names())


result_df = pd.concat([df, word_count_df], axis=1)

print(result_df)