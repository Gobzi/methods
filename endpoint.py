import requests
import argparse

methods = ['get', 'put','post','head','patch','delete']

parser = argparse.ArgumentParser(description='Checks all Methods for a single API endpoint')
parser.add_argument('--url',  type=str, required=True, help='Enter the url')
args = parser.parse_args()
endpoint=(args.url)
print (endpoint)

for i in methods:
    req=requests.request(i, args.url)
    code =req.status_code
    text = req.text
    rsp = '"error":"Internal Server Error"'
    print (code)
    print (text)
