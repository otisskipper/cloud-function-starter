# This is an example of how to make an authorized call to a cloud function
# It requires locally storing a service account key

from google.oauth2 import service_account 
from google.auth.transport.requests import AuthorizedSession
import os
keypath = os.getcwd() + '../local-svc-key.json'
body = {'name': 'Otis'}
base_url='https://us-west1-cd-testing-dev.cloudfunctions.net/test-https2'
creds=service_account.IDTokenCredentials.from_service_account_file(keypath, target_audience=base_url)
authed_session = AuthorizedSession(creds)
# make authenticated request and print the response, status_code
resp = authed_session.get(base_url, body)
print(resp.status_code)
print(resp.text)