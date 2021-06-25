#!/usr/bin/env python

import csv, urllib

f=open('citations.csv','rb')
reader=csv.reader(f)

any='ccc'
for row in reader:
	if not(any==row[6]):
		any=row[6]
		print '= '+any
	print ': {[http://scholar.google.com/scholar?'+urllib.urlencode({'q' : row[1]})+' '+row[1]+']} in '+row[2]+' by '+row[0]

f.close()
