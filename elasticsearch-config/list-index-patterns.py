#!/usr/bin/python
# This script lists the current index patterns

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

# List repository

path = '.kibana/_search' # snapshot name
url = host + path

payload = {
  "_source": ["index-pattern.title"],
  "query": {
    "term": {
      "type": "index-pattern"
    }
  }
}

print(url)

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(url)
r = requests.post(url, auth=awsauth)

print(r)
print(r.status_code)
print(r.text)
