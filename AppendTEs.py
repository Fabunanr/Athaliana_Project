import csv
import itertools

hi = open('alllow_sorted2020id.gff3','rU')
# low = open('Low.txt','r')
# Superfamily_class = open('/Users/rudyfabunan/Documents/TEandSelection/test/ForReferecne/Class_Superfamily_unique.txt','r')
# Family_Superfamily = open('/Users/rudyfabunan/Documents/TEandSelection/test/ForReferecne/TE_Family_Superfamily_unique.txt','r')
test = open('testfile.txt','w')
testwriter = csv.writer(test, delimiter = '\t')

hireader = csv.reader(hi,delimiter = '\t')
# lowreader = csv.reader(low,delimiter = '\t')
# Superfamily_class_reader = csv.reader(Superfamily_class,delimiter = '\t')
# Family_Superfamily_reader = csv.reader(Family_Superfamily,delimiter = '\t')

Superfamiy_class_d = {}
Family_Superfamily_d = {}
TE_toFamily_d = {}

## function for writing to the dictionary
## given information from a tab delimited text file
with open('/Users/rudyfabunan/Documents/TEandSelection/test/results.tsv') as q:
    for line in q:
        elements = line.rstrip('\n').split('\t')
        TE_toFamily_d[elements[0]] = elements[1:]
with open('/Users/rudyfabunan/Documents/TEandSelection/test/ForReference/Class_Superfamily_unique.txt') as f:
    for line in f:
        elements = line.rstrip('\n').split('\t')
        Superfamiy_class_d[elements[0]] = elements[1:]
with open('/Users/rudyfabunan/Documents/TEandSelection/test/ForReference/TE_Family_Superfamily_unique.txt','r') as r:
    for line in r:
        elements = line.rstrip('\n').split('\t')
        Family_Superfamily_d[elements[0]] = elements[1:]

## cleaning up the dictionary
for k, v in TE_toFamily_d.items():
    TE_toFamily_d[k] = str(v).strip('[')
for k, v in TE_toFamily_d.items():
    TE_toFamily_d[k] = str(v).strip(']')
for k, v in TE_toFamily_d.items():
    TE_toFamily_d[k] = str(v).strip("''")

for k, v in Superfamiy_class_d.items():
    Superfamiy_class_d[k] = str(v).strip('[')
for k, v in Superfamiy_class_d.items():
    Superfamiy_class_d[k] = str(v).strip(']')
for k, v in Superfamiy_class_d.items():
    Superfamiy_class_d[k] = str(v).strip("''")

for k, v in Family_Superfamily_d.items():
    Family_Superfamily_d[k] = str(v).strip('[')
for k, v in Family_Superfamily_d.items():
    Family_Superfamily_d[k] = str(v).strip(']')
for k, v in Family_Superfamily_d.items():
    Family_Superfamily_d[k] = str(v).strip("''")

list = []

for row in hireader:
    # rows.append(row)
    try:
        list.append(row + [TE_toFamily_d[row[8]]])
    except KeyError:
        list.append(row + ['unknown'])
        continue

list2 = []
print(list)
for i in list:
    try:
        list2.append(i + [Family_Superfamily_d[i[9]]])
    except KeyError:
        list2.append(i + ['Unknown'])
        continue
for f in list2:
    try:
        testwriter.writerow(f + [Superfamiy_class_d[f[10]]])
    except KeyError:
        testwriter.writerow(f + ['UNknown'])
# for i,j in zip(list,rows):
#     testwriter.writerow([i] + j)
hi.close()
# low.close()
# Superfamily_class.close()
# Family_Superfamily.close()
