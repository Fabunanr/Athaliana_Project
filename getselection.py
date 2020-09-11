import csv
from itertools import islice

high_pg = open('/Users/rudyfabunan/Documents/Final_DataSets/PopulationGenetics_ANGSD/LOW.txt.thetasWindow.gz.pestPG','rU')
Genes = open('results.tsv','rU')
output = open('test.txt','w')

# high_pg_read = high_pg.readlines()

high_pg_r = csv.reader(high_pg,delimiter = '\t')
next(high_pg_r,None)
genes_r = csv.reader(Genes,delimiter = '\t')
high_writer = csv.writer(output,delimiter = '\t')


high_writer.writerow(['Gene']+['TajD'])
for i in genes_r:
    length = int((float(i[6])-float(i[5]))/1000)
    print 'Working on: ' + i[1]
    for l,row in enumerate(high_pg_r):
        x = []
        n = l -1
        end = n + length + 1
        if i[0] == row[1]:
            if float(i[5]) <= float(row[2]) and float(i[6]) >= float(row[2]):
                print str(l) + '\t'+ row[2]+ '\t' + row[8]+ '\t' + str(n) + '\t' + str(end)
    high_pg.seek(0)
