import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(video_data):
    """Preprocess the collected video data."""
    df = pd.DataFrame(video_data)
    df.drop_duplicates(subset=['video_id'], inplace=True)
    df.fillna('', inplace=True)
    return df

def analyze_keywords(df):
    """Perform keyword analysis using TF-IDF."""
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['title'] + ' ' + df['description'])
    return vectorizer.get_feature_names_out()
