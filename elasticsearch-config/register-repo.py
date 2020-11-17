#!/usr/bin/python
# This script registers an s3 bucket and associates it with an ElasticSearch
# repository name.

import boto3
import requests
from requests_aws4auth import AWS4Auth

#logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /
region = 'us-east-2' # e.g. us-west-1
service = 'es'

# The backup name
snapshot_repo_name = 'snapshot-repo' # This is usually the name, don't change
# The bucket name
bucket_name = 'cadre-logging-es-snapshots'
# The s3 endpoint
s3_endpoint = 's3.amazonaws.com'
# The snapshot role that allows ElasticSearch to access S3.  This is the
# CADREElasticSearchSnapshotRole.
snapshot_role_arn = ''

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

# Register repository

path = '_snapshot/' + snapshot_repo_name # the Elasticsearch API endpoint
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": bucket_name,
    "endpoint": s3_endpoint, # for us-east-1
    #"region": "us-east-2", # for all other regions
    "role_arn": snapshot_role_arn
  }
}

print(url)

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)
