#!/usr/bin/python

import boto3
import requests
from requests_aws4auth import AWS4Auth

# ElasticSearch logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /

# The name of the index the alias is attached to, e.g. janus-server-gremlin-1.
index = ''
# The alias to be deleted.  It is of the form 'alias-cadre-<index>', e.g.
# 'alias-cadre-janus-server-gremlin'
alias = ''

region = 'us-east-2' # e.g. us-west-1
service = 'es'

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

path = 'janus-server-gremlin-1/_aliases/alias-janus-server-gremlin'
path = index + '/' + '_aliases/' + alias
url = host + path

payload = {
  "actions": [
   {
      "delete": {
        "alias": alias,
      }
    }
  ]
}


r = requests.delete(url, auth=awsauth)

print(r)
print(r.status_code)
print(r.text)
