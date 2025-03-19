import pandas as pd
from sklearn.cluster import KMeans

def cluster_expenses(df):
    X = df[['amount']]
    
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X)

    print("\nExpense Clustering:\n", df)
    return df
