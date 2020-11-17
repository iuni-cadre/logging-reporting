#!/usr/bin/python

import boto3
import requests
from requests_aws4auth import AWS4Auth

# ElasticSearch logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /

region = 'us-east-2' # e.g. us-west-1
service = 'es'

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

path = '_template?pretty'
url = host + path

r = requests.get(url, auth=awsauth)

print(r)
print(r.status_code)
print(r.text)
