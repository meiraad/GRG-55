import boto3
import json

print('Loading function...')

def lambda_handler(message, context):
    print("Received message from Step Functions:")
    print(message)

    source = message['SourceBucket']
    key = message['SourceObjectKey']
    dest = message['DestinationBucket']

    s3 = boto3.resource('s3')

    copy_source = {
        'Bucket': source,
        'Key': key
    }

    bucket = s3.Bucket(dest)

    bucket.copy(copy_source, 'sample.txt')

    print('Single File is copied')
    