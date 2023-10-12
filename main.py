import os
from pathlib import Path
from datetime import datetime
from io import StringIO
from google.cloud import storage, bigquery
from google.cloud.storage import Client, transfer_manager
from google.oauth2.service_account import Credentials
import pandas as pd

bucket_name = "YOUR_BUCKET_ID"
dataset_name = 'YOUR_DATASET_ID'
repo = 'https://github.com/sfrechette/adventureworks-neo4j.git'

def upload_directory_with_transfer_manager(bucket_name, source_directory, credentials, processes=8):
    storage_client = Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    directory_as_path_obj = Path(source_directory)
    print(directory_as_path_obj)
    paths = directory_as_path_obj.rglob("*")
    file_paths = [path for path in paths if path.is_file()]
    relative_paths = [path.relative_to(source_directory) for path in file_paths]
    string_paths = [str(path) for path in relative_paths]

    print("Found {} files.".format(len(string_paths)))

    # Start the upload.
    results = transfer_manager.upload_many_from_filenames(
        bucket, string_paths, source_directory=source_directory, max_workers=processes
    )

    for name, result in zip(string_paths, results):
        if isinstance(result, Exception):
            print("Failed to upload {} due to exception: {}".format(name, result))
        else:
            print("Uploaded {} to {}.".format(name, bucket.name))


# Upload csv files into BigQuery tables
def load_into_BQ(bucket_name, dataset_name, credentials):
    storage_client = storage.Client(credentials=credentials)
    bigqueryClient = bigquery.Client(credentials=credentials)
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(f'Creating table from {blob.name}')

        insertDate = datetime.utcnow()

        tableRef = bigqueryClient.dataset(dataset_name).table(blob.name.split("/")[-1].rsplit(".", 1)[0])

        csv_data = blob.download_as_string()
        csv_data = csv_data.decode(encoding='latin-1')
        #csv_data.decode("utf-8")
        dataFrame = pd.read_csv(StringIO(csv_data),encoding='latin-1')
        dataFrame['inserted_at'] = insertDate

        bigqueryJob = bigqueryClient.load_table_from_dataframe(dataFrame, tableRef)
        bigqueryJob.result()


if __name__ == '__main__':

    source_file_name = os.path.join('adventureworks-neo4j', 'data')
    creds = Credentials.from_service_account_file(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

    if os.path.exists(source_file_name):
        print(f"The path {source_file_name} exists.")
    else:
        print(f"Cloning {repo} repository...")
        str_clone = f"git clone {repo}"
        os.system(str_clone)

    upload_directory_with_transfer_manager(bucket_name, source_file_name, creds)

    try:
        load_into_BQ(bucket_name, dataset_name, creds)
    except Exception as e:
        print(e)