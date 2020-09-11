import csv,sys
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def readfile(inputfile):
    with open(inputfile) as inf:
        list = []
        csvreader = csv.reader(inf, delimiter='\t')
        for row in csvreader:
            list.append(row[8])
        return(list[1:]) #if the file has a header

highlist = readfile(sys.argv[1])
lowlist = readfile(sys.argv[2])

print('HEP has ',len(highlist),'TEIs','\nHEP has ',len(set(highlist)),'unique TEs')
print('LEP has ',len(lowlist),'TEIs','\nLEP has ',len(set(lowlist)),'unique TEs')

venn2([set(highlist),set(lowlist)], set_labels = ('HEP','LEP'), set_colors = ('Blue','Orange'))
plt.show()
