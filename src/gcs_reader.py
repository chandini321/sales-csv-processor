
from google.cloud import storage
import pandas as pd
from io import BytesIO


def read_csv_from_gcs(bucket_name, file_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    csv_data = blob.download_as_bytes()

    df = pd.read_csv(BytesIO(csv_data))

    return df
