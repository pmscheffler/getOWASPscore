from math import fabs
from xml.etree.ElementInclude import include
import requests
import json
import pprint
import urllib3
import datetime
import getopt, sys

urllib3.disable_warnings()


def getOWASPscore(argv):
    bigip_host = "hostname or IP"
    username = "admin"
    hiddenpassword = "SomePassword"
    policyName = ""
    policyId = ""

    try:
        opts, args = getopt.getopt(argv, "?h:u:p:n:", ["host=", "user=", "password=", "name="])
    except getopt.GetoptError:
        print('Show policy audit details.')
        print('-? getOWASPscore.py')
        print('-h <hostname or ip> (host=)')
        print('-u <username> (username=)')
        print('-p <password> (password=)')
        print('-d <policyID> (id=)')
        print('Format is policyName = "?$filter=name eq policy-name"')
        print('Leave it blank and it will iterate thru all of the policies')
        print('or if you use a wildcard it will go thru a subset')
        print('or the actual name will pull one policy')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-?":
            print('Show policy audit details.')
            print('-? getOWASPscore.py')
            print('-h <hostname or ip> (host=)')
            print('-u <username> (username=)')
            print('-p <password> (password=)')
            print('-d <policyid> (id=) OR -n <policyname> (name=) == One of these are required')
            sys.exit(1)
        elif opt in ("-h", "--host"):
            bigip_host = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            hiddenpassword = arg
        elif opt in ("-n", "--name"):
            policyName = arg
        elif opt in ("-d", "--id"):
            policyId = arg

    url = "https://" + bigip_host + "/mgmt/shared/authn/login"

    payload = json.dumps({
        "username": username,
        "password": hiddenpassword,
        "loginProviderName": "tmos"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False)

    data = json.loads(response.text)

    authToken = data['token']['token']

    headers = {
      'Content-type': 'application/json',
      'X-F5-Auth-Token': authToken
    }

    if len(policyId) == 0:
      url = "https://"+ bigip_host + "/mgmt/tm/asm/policies?$filter=name eq " + policyName
      response = requests.request("GET", url, headers=headers, verify=False)
      data = json.loads(response.text)
      policyId = data['items'][0]['id']
      # pprint.pprint(policyId)

    if len(policyId) > 0:
      url = "https://"+ bigip_host + "/mgmt/tm/asm/owasp/generate-score"

      payload = "{\n    \"policyId\": " + policyId + " \n}"

      response = requests.request("POST", url, headers=headers, data=payload, verify=False)

      print(response.text)


if __name__ == "__main__":
  getOWASPscore(sys.argv[1:])