from google.cloud import firestore

def is_file_processed(file_name):
    db = firestore.Client()

    document_id = file_name.replace("/", "_")
    document = db.collection("processed_files").document(document_id)

    result = document.get()
    return result.exists


def mark_file_processed(file_name):
    db = firestore.Client()

    document_id = file_name.replace("/", "_")
    document = db.collection("processed_files").document(document_id)

    document.set({
        "file_name": file_name,
        "status": "completed"
    })