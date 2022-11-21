import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
methods = ['get', 'put','post','head','patch','delete']


parser = argparse.ArgumentParser(description='Checks all Methods for a single API endpoint')
parser.add_argument('--url',  type=str, required=True, help='Enter the url')
parser.add_argument('--header',  type=str, required=False, help='Enter headers')
args = parser.parse_args()



endpoint=(args.url)
print (args.header)
headers = {args.header.split(':')[0]:args.header.split(':')[1].replace(" ", "")}
print (headers)

for i in methods:
    req=requests.request(i, endpoint, headers=headers, proxies=proxies, verify=False)
    code =req.status_code
    text = req.text
    rsp = '"error":"Internal Server Error"'
    print (i.upper(),"-",code)
    print (text)
