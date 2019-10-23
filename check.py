#!/usr/bin/python
import requests
import csv

host = csv.reader(open("domains.csv","rb"), delimiter=' ', quotechar='|')
list_csv = list(host)
directory = ['/.git', '/.gitignore', '/.git/HEAD', '/.git/object/info/packs', '/protected', '/protected/runtime', '/protected/runtime/application.log']
for h in list_csv:
    for d in directory:
        f = h[0] + d
        r = requests.get(f)
        print f + ' | ' + r.status_code
