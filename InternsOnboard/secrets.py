

import boto3
import json

client = boto3.session.Session().client(service_name='secretsmanager', region_name='us-east-2')

response = client.get_secret_value(
    SecretId='arn:aws:secretsmanager:us-east-2:196626650470:secret:AWS_DJANGO_SECRETS_INTERNSONBOARD-OjGTXE',
)

# print(response['SecretString'])
AWS_ACCESS_KEY_ID_1 = json.loads(response['SecretString'])['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY_1 = json.loads(response['SecretString'])['AWS_SECRET_ACCESS_KEY']

# print(AWS_ACCESS_KEY_ID_1, AWS_SECRET_ACCESS_KEY_1)