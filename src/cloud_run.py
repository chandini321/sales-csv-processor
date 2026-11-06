
import functions_framework

from src.processor import calculate_metrics
from src.gcs_writer import write_json_to_gcs
from src.firestore_tracker import (
    is_file_processed,
    mark_file_processed
)


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

    # Check whether the file was already processed
    if is_file_processed(file_name):
        print("File already processed:", file_name)
        return

    # Calculate metrics
    metrics = calculate_metrics(
        bucket_name,
        file_name
    )

    # Generate report name
    report_name = (
        "reports/"
        + file_name.split("/")[-1].replace(".csv", "_metrics.json")
    )

    # Write JSON report
    write_json_to_gcs(
        bucket_name,
        report_name,
        metrics
    )

    # Mark file as processed
    mark_file_processed(file_name)

    print("Processing completed:", file_name)
