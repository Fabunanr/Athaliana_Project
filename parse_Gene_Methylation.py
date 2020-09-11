import csv

HI = open('High_Methyl_Genes_CGCHGCHH.txt','r')
LOW = open('Low_Methyl_Genes_CGCHGCHH.txt','r')

HI_CG_Genebody_25th = 0.0080
HI_CG_Genebody_75th = 0.2080
LOW_CG_Genebody_25th = 0.0070
LOW_CG_Genebody_75th = 0.1710

HI_r = csv.reader(HI,delimiter='\t')
LOW_r = csv.reader(LOW,delimiter='\t')

def pullgenes(pop,percentlevel,actnum,out):
    outf = open(out,'w')
    out_r = csv.writer(outf,delimiter = '\t')
    if percentlevel == '25':
        for row in pop:
            if row[1] == 'CG':
                if float(row[4]) <= float(actnum):
                    out_r.writerow(row)
    elif percentlevel == '75':
        for row in pop:
            if row[1] == 'CG':
                if float(row[4]) >= float(actnum):
                    out_r.writerow(row)


# pullgenes(HI_r,'25',HI_CG_Genebody_25th,'HEP_CG_LowMethylatedGenes.txt')
pullgenes(HI_r,'75',HI_CG_Genebody_75th,'HEP_CG_HighlyMethylatedGenes.txt')
# pullgenes(LOW_r,'25',LOW_CG_Genebody_25th,'LEP_CG_LowMethylatedGenes.txt')
# pullgenes(LOW_r,'75',LOW_CG_Genebody_75th,'LEP_CG_HighlyMethylatedGenes.txt')
