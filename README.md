# Quick POC of getting OWASP Scores for a selected Policy

## Introduction

With this script you can get the values of the OWASP Compliance report from your BIG-IP AWAF

## Install and Running

You need to run it with access to the Management IP and with a user/pw combo that has Security Admin capabilities

The parameters are: 
  * -h/host for the management port 
  * -u/user for the user 
  * -p/password  (note that there's a call to get an Auto Token)
  * -n/name or -d/id for either the Policy Name or the Policy ID

Output is the JSON from the call in raw format.  You can pipe this to jq and query for specific items

**Note** that this is offereed as an example and no warranty or other protections are offered...
please use with care

