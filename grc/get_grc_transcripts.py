#!/usr/bin/python3

import requests
import time
import os

root_url = 'https://www.grc.com/sn/sn-'
found_it = False
show_number = 0


for u in range(1,850):
    if u < 10:
        num = '00{}'.format(str(u))
    elif u < 100:
        num = '0{}'.format(str(u))
    else:
        num = str(u)
    url_to_search = '{}{}.txt'.format(root_url,num)
    if not os.path.exists('/Users/chris/code/grc/shows/{}.txt'.format(num)):
        r = requests.get(url_to_search)
        with open('/Users/chris/code/grc/shows/{}.txt'.format(num),'w+') as tw:
            tw.write(r.text)
        time.sleep(1)

