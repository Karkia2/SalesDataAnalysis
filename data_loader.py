import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    df = df.drop_duplicates()
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
    df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    df['Month'] = df['Order Date'].dt.month
    df['Hour'] = df['Order Date'].dt.hour
    df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip())
    return df
