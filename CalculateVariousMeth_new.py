import pandas as pd
import csv
import numpy as np
import scipy.stats as sp

hi = open('HI_Appended_TEIs.txt','r')
low = open('LOW_Appended_TEIs.txt','r')
methhiCG = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/HIGH_noMidGroups.feature.CG.txt','r')
methhiCHG = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/HIGH_noMidGroups.feature.CHG.txt','r')
methhiCHH = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/HIGH_noMidGroups.feature.CHH.txt','r')
methlowCG = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/Low_noBOS.feature.CG.txt','r')
methlowCHG = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/Low_noBOS.feature.CHG.txt','r')
methlowCHH = open('/Users/rudyfabunan/Documents/Final_DataSets/MethylationAnalysis/TE_and_TEgenes/Low_noBOS.feature.CHH.txt','r')

## read files
hi_r = csv.reader(hi, delimiter = '\t')
low_r = csv.reader(low, delimiter = '\t')
methhiCG_r = csv.reader(methhiCG, delimiter = '\t')
next(methhiCG_r,None)
methhiCHG_r = csv.reader(methhiCHG, delimiter = '\t')
methhiCHH_r = csv.reader(methhiCHH, delimiter = '\t')
methlowCG_r = csv.reader(methlowCG, delimiter = '\t')
methlowCHG_r = csv.reader(methlowCHG, delimiter = '\t')
methlowCHH_r =csv.reader(methlowCHH, delimiter = '\t')

hi_list = []
low_list = []
MethHi_CGlist =[]
MethHi_CHGlist =[]
MethHi_CHHlist =[]
MethLow_CGlist =[]
MethLow_CHGlist =[]
MethLow_CHHlist =[]

def appendlists(which,whichlist):
    for row in which:
        whichlist.append(row)

appendlists(hi_r,hi_list)
appendlists(low_r,low_list)
appendlists(methhiCG_r,MethHi_CGlist)
appendlists(methhiCHG_r,MethHi_CHGlist)
appendlists(methhiCHH_r,MethHi_CHHlist)
appendlists(methlowCG_r,MethLow_CGlist)
appendlists(methlowCHG_r,MethLow_CHGlist)
appendlists(methlowCHH_r,MethLow_CHHlist)

hi_df = pd.DataFrame(hi_list)
low_df = pd.DataFrame(low_list)
MethHI_CG_df = pd.DataFrame(MethHi_CGlist)
MethHI_CHG_df = pd.DataFrame(MethHi_CHGlist)
MethHI_CHH_df = pd.DataFrame(MethHi_CHHlist)
MethLow_CG_df = pd.DataFrame(MethLow_CGlist)
MethLow_CHG_df = pd.DataFrame(MethLow_CHGlist)
MethLow_CHH_df = pd.DataFrame(MethLow_CHHlist)

hi_classi = hi_df.loc[hi_df[0] == 'ClassI', 3].iloc[0:].tolist()
hi_classii = hi_df.loc[hi_df[0] == 'ClassII', 3].iloc[0:].tolist()
hi_dna = hi_df.loc[hi_df[1] == 'DNA', 3].iloc[0:].tolist()
hi_dna_Enspm = hi_df.loc[hi_df[1] == 'DNA/En-Spm', 3].iloc[0:].tolist()
hi_dna_Hat = hi_df.loc[hi_df[1] == 'DNA/HAT', 3].iloc[0:].tolist()
hi_dna_Harbinger = hi_df.loc[hi_df[1] == 'DNA/Harbinger', 3].iloc[0:].tolist()
hi_dna_Mariner = hi_df.loc[hi_df[1] == 'DNA/Mariner', 3].iloc[0:].tolist()
hi_dna_MuDR = hi_df.loc[hi_df[1] == 'DNA/MuDR', 3].iloc[0:].tolist()
hi_dna_Pogo = hi_df.loc[hi_df[1] == 'DNA/Pogo', 3].iloc[0:].tolist()
hi_LINE_L1 = hi_df.loc[hi_df[1] == 'LINE/L1', 3].iloc[0:].tolist()
hi_LINE = hi_df.loc[hi_df[1] == 'LINE?', 3].iloc[0:].tolist()
hi_LTR_Copia = hi_df.loc[hi_df[1] == 'LTR/Copia', 3].iloc[0:].tolist()
hi_LTR_Gypsy = hi_df.loc[hi_df[1] == 'LTR/Gypsy', 3].iloc[0:].tolist()
hi_RC_Helitron = hi_df.loc[hi_df[1] == 'RC/Helitron', 3].iloc[0:].tolist()
hi_unknown = hi_df.loc[hi_df[1] == 'unknown', 3].iloc[0:].tolist()

low_classi = low_df.loc[low_df[0] == 'ClassI', 3].iloc[0:].tolist()
low_classii = low_df.loc[low_df[0] == 'ClassII', 3].iloc[0:].tolist()
low_dna = low_df.loc[low_df[1] == 'DNA', 3].iloc[0:].tolist()
low_dna_Enspm = low_df.loc[low_df[1] == 'DNA/En-Spm', 3].iloc[0:].tolist()
low_dna_Hat = low_df.loc[low_df[1] == 'DNA/HAT', 3].iloc[0:].tolist()
low_dna_Harbinger = low_df.loc[low_df[1] == 'DNA/Harbinger', 3].iloc[0:].tolist()
low_dna_Mariner = low_df.loc[low_df[1] == 'DNA/Mariner', 3].iloc[0:].tolist()
low_dna_MuDR = low_df.loc[low_df[1] == 'DNA/MuDR', 3].iloc[0:].tolist()
low_dna_Pogo = low_df.loc[low_df[1] == 'DNA/Pogo', 3].iloc[0:].tolist()
low_LINE_L1 = low_df.loc[low_df[1] == 'LINE/L1', 3].iloc[0:].tolist()
low_LINE = low_df.loc[low_df[1] == 'LINE?', 3].iloc[0:].tolist()
low_LTR_Copia = low_df.loc[low_df[1] == 'LTR/Copia', 3].iloc[0:].tolist()
low_LTR_Gypsy = low_df.loc[low_df[1] == 'LTR/Gypsy', 3].iloc[0:].tolist()
low_RC_Helitron = low_df.loc[low_df[1] == 'RC/Helitron', 3].iloc[0:].tolist()
low_unknown = low_df.loc[low_df[1] == 'unknown', 3].iloc[0:].tolist()


def getvalues(set,himethylcontextfile,lowmethylcontext,methylcontext,setname):
    pmthi = []
    genehi = []
    pmtlow = []
    genelow =[]
    for i in himethylcontextfile:
        if i[0] in set:
            pmthi.append(i[1])
            genehi.append(i[2])
    for i in lowmethylcontext:
        if i[0] in set:
            pmtlow.append(i[1])
            genelow.append(i[2])
    pmthi = [float(i) for i in pmthi]
    genehi = [float(i) for i in genehi]
    pmtlow = [float(i) for i in pmtlow]
    genelow = [float(i) for i in genelow]
    try:
        print('The HEP ' + str(methylcontext) + ' pmt values for '+ setname  + ' are: ' )
        print np.average(pmthi)
        print sp.stats.describe(pmthi)
        print('The HEP ' + str(methylcontext) + ' gene values for '+ setname + ' are: ')
        print np.average(genehi)
        print sp.stats.describe(genehi)
        print('The LEP ' + str(methylcontext) + ' pmt values for '+ setname  + ' are: ' )
        print np.average(pmtlow)
        print sp.stats.describe(pmtlow)
        print('The LEP ' + str(methylcontext) + ' gene values for '+ setname + ' are: ')
        print np.average(genelow)
        print sp.stats.describe(genelow)
    except ValueError:
        print setname + 'nothin here..'

## shared
ClassI_shared = set(hi_classi).intersection(low_classi)
ClassII_shared = set(hi_classii).intersection(low_classii)
DNA_shared = set(hi_dna).intersection(low_dna)
DNA_En_Spm_shared = set(hi_dna_Enspm).intersection(low_dna_Enspm)
DNA_HAT_shared = set(hi_dna_Hat).intersection(low_dna_Hat)
DNA_Harbinger_shared = set(hi_dna_Harbinger).intersection(low_dna_Harbinger)
DNA_Mariner_shared = set(hi_dna_Mariner).intersection(low_dna_Mariner)
DNA_MuDR_shared = set(hi_dna_MuDR).intersection(low_dna_MuDR)
DNA_Pogo_shared = set(hi_dna_Pogo).intersection(low_dna_Pogo)
LINE_L1_shared = set(hi_LINE_L1).intersection(low_LINE_L1)
LINE_shared = set(hi_LINE).intersection(low_LINE)
LTR_Copia_shared = set(hi_LTR_Copia).intersection(low_LTR_Copia)
LTR_Gypsy_shared = set(hi_LTR_Gypsy).intersection(low_LTR_Gypsy)
RC_Helitron_shared = set(hi_RC_Helitron).intersection(low_RC_Helitron)
unknown_shared = set(hi_unknown).intersection(low_unknown)

## unique values
ClassI_hi = list(set(hi_classi) - set(low_classi))
ClassII_hi = list(set(hi_classii) - set(low_classii))
ClassI_low = list(set(low_classi) - set(hi_classi))
ClassII_low =  list(set(low_classii) - set(hi_classii))

DNA_low = list(set(low_dna) - set(hi_dna))
DNA_EnSpm_low = list(set(low_dna_Enspm) - set(hi_dna_Enspm))
DNA_HAT_low = list(set(low_dna_Hat) - set(hi_dna_Hat))
DNA_Harbinger_low = list(set(low_dna_Harbinger) - set(hi_dna_Harbinger))
DNA_Mariner_low = list(set(low_dna_Mariner) - set(hi_dna_Mariner))
DNA_MuDR_low = list(set(low_dna_MuDR) - set(hi_dna_MuDR))
DNA_Pogo_low = list(set(low_dna_Pogo) - set(low_dna_Pogo))
LINE_L1_low = list(set(low_LINE_L1) - set(hi_LINE_L1))
LINE_low = list(set(low_LINE) - set(hi_LINE))
LTR_Copia_low = list(set(low_LTR_Copia) - set(hi_LTR_Copia))
LTR_Gypsy_low = list(set(low_LTR_Gypsy) - set(hi_LTR_Gypsy))
RC_Helitron_low = list(set(low_RC_Helitron) - set(hi_RC_Helitron))
unknown_low = list(set(low_unknown) - set(hi_unknown))

DNA_high =list(set(hi_dna) - set(low_dna))
DNA_EnSpm_high =list(set(hi_dna_Enspm) - set(low_dna_Enspm))
DNA_HAT_high =list(set(hi_dna_Hat) - set(low_dna_Hat)  )
DNA_Harbinger_high=list(set(hi_dna_Harbinger) - set(low_dna_Harbinger)  )
DNA_Mariner_high =list(set(hi_dna_Mariner) - set(low_dna_Mariner)  )
DNA_MuDR_high =list(set(hi_dna_MuDR) - set(low_dna_MuDR)  )
DNA_Pogo_high =list(set(hi_dna_Pogo) - set(low_dna_Pogo)  )
LINE_L1_high =list(set(hi_LINE_L1) - set(low_LINE_L1)   )
LINE_high =list(set(hi_LINE) -set(low_LINE)   )
LTR_Copia_high =list(set(hi_LTR_Copia) - set(low_LTR_Copia)  )
LTR_Gypsy_high =list(set(hi_LTR_Gypsy) - set(low_LTR_Gypsy)  )
RC_Helitron_high =list(set(hi_RC_Helitron) - set(low_RC_Helitron)  )
unknown_high =list(set(hi_unknown) - set(low_unknown) )

sets = [ClassI_shared,ClassII_shared,DNA_shared,DNA_En_Spm_shared,DNA_HAT_shared]
names = ['ClassI shared','ClassII shared','DNA shared','DNA/En-Spm shared','DNA/HAT shared']
for i,j in zip(sets,names):
    getvalues(i,MethHi_CGlist,MethLow_CGlist,'CG',j)
