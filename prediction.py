import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

def predict_expenses(df):
    predictions = {}

    for bill in df['name']:
        past_values = df[df['name'] == bill]['amount'].tolist()
        
        if len(past_values) > 1:  # Ensure we have enough data points
            model = SimpleExpSmoothing(past_values).fit(smoothing_level=0.5, optimized=False)
            predicted_amount = model.forecast(1)[0]
            predictions[bill] = predicted_amount

    print("\nPredicted Bills for Next Month:")
    for bill, amount in predictions.items():
        print(f"{bill}: ${amount:.2f}")

    return predictions
