import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

def predict_expenses(df):
    predictions = {}

    if len(df["month"].unique()) < 3:
        print("\n❗ Not enough data for prediction. Please enter at least 3 months of bills.\n")
        return None

    for bill in df["name"].unique():
        past_values = df[df["name"] == bill].sort_values("month")["amount"].tolist()

        if len(past_values) >= 3:  # Predict only if we have at least 3 data points
            model = SimpleExpSmoothing(past_values).fit(smoothing_level=0.5, optimized=False)
            predicted_amount = model.forecast(1)[0]
            predictions[bill] = predicted_amount

    print("\n📊 Predicted Bills for Next Month:")
    for bill, amount in predictions.items():
        print(f"{bill}: ${amount:.2f}")

    return predictions
