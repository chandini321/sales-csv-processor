
import pandas as pd


def calculate_metrics(csv_file):
    df = pd.read_csv(csv_file)

    metrics = {
        "row_count": len(df),
        "null_counts": df.isnull().sum().to_dict()
    }

    return metrics
