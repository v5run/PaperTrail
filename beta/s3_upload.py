from beta.sk import aws_access_key, aws_secret_key
import boto3

def upload_to_s3(file_name, bucket_name='paper-trail-receipt-dump'):
    client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    try:
        upload_file_key = 'receipts/' + file_name.split('/')[-1] # directory in s3
        client.upload_file(file_name, bucket_name, upload_file_key)
        print(f"File {file_name} uploaded to {bucket_name}")
    except Exception as e:
        print(f"Error uploading file {file_name} to {bucket_name}")
        print(e)