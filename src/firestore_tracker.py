from google.cloud import firestore


def is_file_processed(file_name):
    db = firestore.Client()

    document = db.collection("processed_files").document(file_name)
    result = document.get()

    return result.exists


def mark_file_processed(file_name):
    db = firestore.Client()

    document = db.collection("processed_files").document(file_name)

    document.set({
        "file_name": file_name,
        "status": "completed"
    })