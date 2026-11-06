
from src.processor import calculate_metrics
from src.gcs_writer import write_json_to_gcs
from src.cloud_run import process_gcs_file


BUCKET_NAME = "sales-csv-processor"

INPUT_FILE = "raw-data/student_assessments.csv"

OUTPUT_FILE = "reports/student_assessments_metrics.json"


def main():
    metrics = calculate_metrics(
        BUCKET_NAME,
        INPUT_FILE
    )

    write_json_to_gcs(
        BUCKET_NAME,
        OUTPUT_FILE,
        metrics
    )


if __name__ == "__main__":
    main()
