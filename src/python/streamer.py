import csv
import os
from io import StringIO
from dotenv import load_dotenv
import os

from google.cloud import storage


load_dotenv()

storage_client = storage.Client()
bucket = storage_client.get_bucket(os.environ.get('BUCKET_NAME'))

blob = bucket.blob(os.environ.get('FILE_NAME'))
blob = blob.download_as_string()
blob = blob.decode('utf-8')

blob = StringIO(blob)  #tranform bytes to string here

print(blob.readlines()[:5])