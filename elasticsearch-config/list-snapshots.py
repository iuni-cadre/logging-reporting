#!/usr/bin/python
# This script lists the snapshots
import boto3
import requests
from requests_aws4auth import AWS4Auth

# ElasticSearch logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /

region = 'us-east-2' # e.g. us-west-1
service = 'es'

# The backup name
snapshot_repo_name = 'snapshot-repo' # This is usually the name, don't change

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

# List repository

path = '_snapshot/' + snapshot_repo_name + '/' + '_all?pretty' # the Elasticsearch API endpoint
url = host + path

print(url)
r = requests.get(url, auth=awsauth)

print(r)
print(r.status_code)
print(r.text)
