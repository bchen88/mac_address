#!/usr/bin/env python
# importing the requests library 
from __future__ import print_function
import requests 
import argparse
import sys
 
#help description
parser = argparse.ArgumentParser(description='Query MAC address')

#command options
parser.add_argument(
    "--search",
    help="MAC Address")

parser.add_argument(
    "--apikey",
    help="Your API key is required!!")

#parse for command options
args = parser.parse_args()

params = {}
keys = ['search']

# get command options
for k in keys:
    if args.__getattribute__(k):
        params[k] = args.__getattribute__(k)

#no three command options are specified
if len(params) == 0:
    parser.print_help()
    sys.exit()

# get API key for MAC address API
if args.__getattribute__('apikey'):
    params['apiKey'] = args.__getattribute__('apikey')
else:
    print("Error: API key must be passed via --apikey=YOUR_KEY ",
          file=sys.stderr)
    sys.exit(1)

#perform request as https://api.macaddress.io/v1?apiKey=value1&output=json&search=value2
# api-endpoint 
URL = "https://api.macaddress.io/v1?"
 
params['output'] = 'json'

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = params) 
 
# extracting data in json format 
data = r.json() 
 
 
# extracting company name and mac address
CompanyName = data['vendorDetails']['companyName'] 
macAddress = data['macAddressDetails']['searchTerm'] 
 
#printing the raw output 
print("------------Complete Raw Output------------")
print(data)
print("")
print("")

print("Company Name: ", CompanyName)
print("MAC Address: ", macAddress)

