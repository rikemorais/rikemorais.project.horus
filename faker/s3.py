import os
import boto3

class DataUploader:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = self._create_s3_client()

    def _create_s3_client(self):
        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        aws_session_token = os.environ.get('AWS_SESSION_TOKEN')

        return boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )

    def upload_to_s3(self, local_file, s3_key):
        self.s3_client.upload_file(local_file, self.bucket_name, s3_key)
        print(f"Arquivo {local_file} enviado para o S3 no caminho {s3_key}.")

# Exemplo de uso da classe DataUploader
bucket_name = 'faker-dev'
s3_key = 'products/'
local_file = '../data/products.parquet'

uploader = DataUploader(bucket_name)
uploader.upload_to_s3(local_file, s3_key)
