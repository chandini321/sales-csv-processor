
from src.gcs_reader import read_csv_from_gcs


def calculate_metrics(bucket_name, file_name):
    df = read_csv_from_gcs(bucket_name, file_name)

    metrics = {
        "file_name": file_name,
        "row_count": len(df),
        "null_counts": df.isnull().sum().to_dict()
    }

    return metrics
