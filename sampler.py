import csv
import sys

obamaID = "P80003338"
mccainID = "P80002801" 

with file(sys.argv[1], 'r') as f:
    for line in f:
        if obamaID or mccainID in item:
            print line[:-1]
			




