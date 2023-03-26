import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

authUrl =  "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
reqUrl = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site-health"

USER = input('Enter your username for DNAC: ')
PASS = getpass('Enter your password for DNAC: ')

payload = {}


headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	}
	
	
repx = requests.post(authUrl, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=payload, verify=False)


tokenJSON = repx.json()

TOKEN = tokenJSON['Token']

print(repx.text)

payload1 = {}


headers1 = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-Auth-Token': TOKEN
	}
		

repy = requests.get(reqUrl, headers=headers1, data=payload1, verify=False)

print(repy.text)

