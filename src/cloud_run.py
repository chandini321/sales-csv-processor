
import functions_framework

from src.processor import calculate_metrics
from src.gcs_writer import write_json_to_gcs


BUCKET_NAME = "sales-csv-processor"


@functions_framework.cloud_event
def process_gcs_file(cloud_event):
    data = cloud_event.data

    bucket_name = data["bucket"]
    file_name = data["name"]

    # Process only CSV files inside raw-data/
    if not file_name.startswith("raw-data/"):
        return

    if not file_name.lower().endswith(".csv"):
        print("Skipping non-CSV file:", file_name)
        return

    metrics = calculate_metrics(
        bucket_name,
        file_name
    )

    report_name = (
        "reports/"
        + file_name.split("/")[-1].replace(".csv", "_metrics.json")
    )

    write_json_to_gcs(
        bucket_name,
        report_name,
        metrics
    )

    print("Processing completed:", file_name)
