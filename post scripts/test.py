#!/usr/bin/env python3
# ========================================== #
# ============== INSTRUCTIONS ============== #
# === Used to test postprocessing script === #
# ========== Enter apikey and url ========== #
# ===== Run script as python3 test.py ====== #
# ========================================== #

watcherapi = ''
watcheraddress = 'http://localhost:9090/'

import json
import sys
import urllib.request
import urllib.parse

data = {}

args = sys.argv

download_dir = input('Download dir (parent of download): ')
guid = input('GUID: ')
name = input('Name: ')

while download_dir[-1] in ['/', '\\']:
    download_dir = download_dir[:-1]

data['apikey'] = watcherapi
data['name'] = name
data['path'] = u'{}/{}'.format(download_dir, name)
data['downloadid'] = guid
data['guid'] = guid
data['mode'] = 'complete'

url = '{}/postprocessing/'.format(watcheraddress)
post_data = urllib.parse.urlencode(data).encode('ascii')

print('========================')
print('URL:')
print(url)
print('========================')
print('POST:')
print(post_data)
print('========================')

request = urllib.request.Request(url, post_data, headers={'User-Agent': 'Mozilla/5.0'})
response = json.loads(urllib.request.urlopen(request, timeout=600).read())

print(json.dumps(response, indent=4, sort_keys=True))

sys.exit(0)

# pylama:ignore=E402
