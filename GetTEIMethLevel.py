import csv
import itertools

high_meth = open('mbin.high.data','r')
# low_meth = open('mbin.low.data','r')
high_TEI = open('/Users/rudyfabunan/Documents/TEandSelection/test/Copia/High_Copia_Regions.txt','rU')
# Low_Copia_TEI = open('/Users/rudyfabunan/Documents/TEandSelection/test/Copia/Low_Copia_Regions.txt','rU')

high_meth_r = csv.reader(high_meth,delimiter = '\t')
# low_meth_r = csv.reader(low_meth,delimiter = '\t')
high_Copia_TEI_r = csv.reader(high_Copia_TEI,delimiter = '\t')
# Low_Copia_TEI_r = csv.reader(Low_Copia_TEI,delimiter = '\t')

output_high = open('High_CopiaTEI_Methlevel.txt','w')
# output_low = open('Low_CopiaTEI_Methlevel.txt','w')

high_writer = csv.writer(output_high,delimiter = '\t')
# low_writer = csv.writer(output_low,delimiter = '\t')

high_writer.writerow('Chrom'+'Program'+'Type'+'Start'+'Stop'+'Meth 1kb upstream'+'Meth within insertion'+'Meth 1kb downstream')
for i in high_Copia_TEI_r:
    for row in high_meth_r:
        if float(row[1]) <= float(i[3]) and float(i[3]) - 1000 <= float(row[2]):
            if row[0] == i[0]:
                high_writer.writerow(i[0:5] + row + high_meth_r.next() + high_meth_r.next())
                # high_writer.writerow(high_meth_r.next())
                # high_writer.writerow(high_meth_r.next())
                high_meth.seek(0)
                break
