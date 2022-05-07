#!/usr/bin/python3

import requests
import time
import osi

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
    r = requests.get(url_to_search)
    with open('/Users/chris/code/grc/shows/{}.txt'.format(num)) as tw:
        tw.write(r.text)

    print('Searching at {}'.format(url_to_search))
    if not r.status_code == 404:
        # term_to_search = 'vulnerability'.lower()
        term_to_search = 'windows 11'.lower()
        if term_to_search in r.text:
            print('------ Found {} in show # {}------'.format(term_to_search, str(num)))
            content = r.text
            lines = content.split('\n')
            for line in lines:
                if not term_to_search in line:
                    print(line)
                    continue
                print('Term in context {}'.format(line))
                break

            found_it = True
            show_number = num 
            break
        else:
            time.sleep(5)
            u+=1

print('Term was found at show number: {}'.format(show_number))
