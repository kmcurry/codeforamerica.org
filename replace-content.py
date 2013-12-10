from sys import argv
from re import compile
from bs4 import BeautifulSoup
from requests import get

pattern = compile(r'^---\n(?P<yaml>(.+\n)*wordpress_id: (?P<id>\d+)(\n.+)*)\n---\n')

for filename in argv[1:]:

    with open(filename) as file:
        match = pattern.match(file.read())
        
        if not match:
            print 'no yaml', filename
            exit(1)
    
    if 'wordpress_html: true' in match.group('yaml'):
        print 'fuck this'
        continue
    
    url = 'http://codeforamerica.org/?p=' + match.group('id')
    
    print 'GET', url, '...'
    resp = get(url)
    
    print resp.status_code, resp.url
    soup = BeautifulSoup(resp.content)
    entry = soup.find('div', dict(id='inner')).find('div', {'class': 'entry-content'})
    
    if not entry:
        print 'no soup', filename
    
    with open(filename, 'w') as file:
        print >> file, '---'
        print >> file, match.group('yaml')
        print >> file, 'wordpress_html: true'
        print >> file, 'wordpress_permalink:', resp.url
        print >> file, '---'
    
        for child in entry:
            file.write(unicode(child).encode('utf-8'))
