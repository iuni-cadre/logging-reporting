#!/usr/bin/python

import boto3
import requests
from requests_aws4auth import AWS4Auth

#logging instance
# Insert the full HTTP address of the ElasticSearch logging server
host = '/' # include https:// and trailing /
region = 'us-east-2' # e.g. us-west-1
service = 'es'

# The name of the template
# The template name should be of the form 'cadre_<index-name>_template' where
# <index-name> is a generic name of the index, e.g.
# 'cadre_interface_error_template'
template = ''
# The index pattern describes the indices the template will be appled to
# The format should be 'cadre-<index-name>*', where <index-name> is as
# described above, e.g. 'cadre-interface-error*'.  The '*' is needed to apply
# to new indices generated during roll overs.
index_pattern = ''
# The policy should name an existing policy created using the Kibana Index
# Management web page.  It is of the form 'cadre_<index-name>_policy', where
# <index> is as describe above, e.g. 'cadre_interface_error_policy'.
index_policy = ''
# The alias is the alias to be assigned a newly created index after a roll over
# occurs.  It is of the form 'alias-cadre-<index>', e.g.
# 'alias-cadre-interface-error'
alias = ''

# Get the credentials to access the ElasticSearch server
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# For debugging purposes
# print(credentials.access_key)
# print(credentials.secret_key)

path = '_template/' + template
url = host + path

payload = {
  "index_patterns": [
    index_pattern
  ],
  "settings": {
    "opendistro.index_state_management.policy_id": index_policy,
    "opendistro.index_state_management.rollover_alias": alias
  }
}


print(url)

headers = {"Content-Type": "application/json"}

print(url)
r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r)
print(r.status_code)
print(r.text)
