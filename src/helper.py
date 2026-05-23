# Helper functions for student success predictor

def load_data(path):
    """Load dataset from given path"""
    import pandas as pd
    return pd.read_csv(path)

def preprocess_data(df):
    """Basic preprocessing: handle missing values"""
    return df.dropna()
