
from google.cloud import storage
import json


def write_json_to_gcs(bucket_name, file_name, metrics):
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    json_data = json.dumps(metrics, indent=4)

    blob.upload_from_string(
        json_data,
        content_type="application/json"
    )

    print(f"Report uploaded: {file_name}")
