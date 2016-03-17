import sys
import pandas as pd
import csv

def ages(filename):
	with open(filename, 'r') as fi:
		reader = csv.DictReader(fi)
		for row in reader:
			yield row['birth_year']

if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
    count = {}
    for i in ages(sys.argv[1]):
    	count[i] = count.get(i,0)+1
    total = sum(count.itervalues())
    current = 0
    for k,v in sorted(count.iteritems()):
		current +=v
		if current*2>=total:
			print 2016-int(k)
			break