# Quick POC of getting OWASP Scores for a selected Policy

## Introduction

With this script you can get the values of the OWASP Compliance report from your BIG-IP AWAF

## Install and Running

You need to run it with access to the Management IP and with a user/pw combo that has Security Admin capabilities

The parameters are: \n
\t-h/host for the management port \n
\t-u/user for the user \n
\t-p/password  (note that there's a call to get an Auto Token)\n
\t-n/name or -d/id for either the Policy Name or the Policy ID\n

Output is the JSON from the call in raw format.  You can pipe this to jq and query for specific items

Note that this is offereed as an example and no warranty or other protections are offered...
please use with care

