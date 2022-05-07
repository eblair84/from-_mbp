import requests

import hashlib
import hmac
import time
import base64
from urllib.parse import quote
import json

json_args = '{"command":"stock_lookup", "symbol":"flnt"}'

secret_key = 'QGe4JazqDjehKRKkkk1cA0bdWzP7ykwCsDlXeRgR'

shared_key = 'PhHjBc5BRtlmFnh250HC'

formatted_args = quote(json_args)

timenow = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

digest = hashlib.sha1

raw_args=json_args+'\n'+timenow

hmac_hash = hmac.new(secret_key.encode(),raw_args.encode(),digest).digest()

sig = base64.b64encode(hmac_hash).rstrip()

url_base = 'https://whalewisdom.com/shell/command.json?'

url_args = 'args=' + formatted_args

url_end = '&api_shared_key=' + shared_key + '&api_sig=' + sig.decode() + '&timestamp=' + timenow

api_url = url_base + url_args + url_end

jr = requests.get(api_url)

js_content = json.loads(jr.text)
# print(content)

link = js_content.get('stocks')[0]['link']
print('link? {}'.format(link))
html = requests.get(link)

print(html.text)


