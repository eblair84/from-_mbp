#!/Users/chris/.virtualenvs/grc/bin/python

import os

color = '\033[95m'
end = '\033[0m'
path_to_shows = '/Users/chris/code/grc/shows'
print('Searching shows-----')

files = os.listdir(path_to_shows)
for f in files:
    with open(os.path.join(path_to_shows,f),'r') as fr:
        content = fr.readlines()
        for line in content:
            if 'vulnerability'.lower() in line:
                line_parts = line.split(' ')
                new_line = ''
                for lp in line_parts:
                    if lp == 'vulnerability'.lower():
                        lp = '{}{}{}'.format(color,lp,end)
                    new_line += '{} '.format(lp)
                print('term was found in show# {}'.format(f))
                print('Context:\n{}'.format(new_line))
