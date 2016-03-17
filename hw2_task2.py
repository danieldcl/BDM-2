import csv
import sys
import dateutil.parser

##################################################
##################################################
def first_ride(reader):
    day = ''
    for row in reader:
        starttime = dateutil.parser.parse(row['starttime']).weekday()
        if starttime != day:
            day = starttime
            yield row


if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as fi:
        reader = csv.DictReader(fi)
        for row in first_ride(reader):
            print ','.join(map(row.get, reader.fieldnames))
            
