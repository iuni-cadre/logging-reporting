#!/usr/bin/python

import boto3
import requests
from requests_aws4auth import AWS4Auth

# ElasticSearch logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /

# ElasticSearch index and alias
# index format is "cadre-<index-name>-1". The "-1" is to indicate the first
# generation of the index for purposes of supporing index roll overs
index = ''
# alias format is "alias-cadre-<index-name>"
alias = ''

region = 'us-east-2' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

path = '_aliases'
url = host + path

payload = {
  "actions": [
   {
      "add": {
        "index": index,
        "alias": alias,
        "is_write_index": "true"
      }
    }
  ]
}


headers = {"Content-Type": "application/json"}

#print(url)
#print
r = requests.post(url, auth=awsauth, json=payload, headers=headers)

print(r)
print(r.status_code)
print(r.text)
