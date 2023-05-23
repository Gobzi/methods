import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


parser = argparse.ArgumentParser(description='Checks all Methods for a single API endpoint')
parser.add_argument('--url',  type=str, required=True, help='Enter the url')
parser.add_argument('--methods',  nargs='+',  type=str, required=True, help='Enter the url')
parser.add_argument('--proxy',  type=str, required=False, help='Enter IP:Port')
parser.add_argument('--header',  type=str, required=False, help='Enter headers')
parser.add_argument('--wordlist',  type=str, required=True, help='Enter path for Wordlist')


args = parser.parse_args()
endpoint=(args.url)
methods=(args.methods)
proxies = {"http": args.proxy, "https": args.proxy}
f = open(args.wordlist, "r")

if args.header:
    headers = {args.header.split(':')[0]:args.header.split(':')[1].replace(" ", "")}
else:
    headers = {}

if not endpoint.startswith("http://") and not endpoint.startswith("https://"):
    print("The URL must start with http:// or https://. Please try again.")
    exit()

for i in methods:
    for line in f:
        endpoint = endpoint + "/" + line.strip()
        req=requests.request(i, endpoint, headers=headers, proxies=proxies, verify=False)
        code =req.status_code
        text = req.text
        rsp = '"error":"Internal Server Error"'
        print (i.upper(),"-",code)
