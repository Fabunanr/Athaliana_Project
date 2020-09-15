import csv
"""
> summary.data.frame(Chr1TajiD.txt)
      all                HI                 LOW                MI
 Min.   :-2.8243   Min.   :-2.629347   Min.   :-2.6032   Min.   :-2.6586
 1st Qu.:-1.5179   1st Qu.:-0.774959   1st Qu.:-1.0785   1st Qu.:-1.0804
 Median :-0.9392   Median : 0.009907   Median :-0.4237   Median :-0.4701
 Mean   :-0.7382   Mean   : 0.066967   Mean   :-0.3149   Mean   :-0.3393
 3rd Qu.:-0.1344   3rd Qu.: 0.814820   3rd Qu.: 0.3042   3rd Qu.: 0.2621
 Max.   : 4.3298   Max.   : 3.761963   Max.   : 4.0074   Max.   : 3.6711
                                                         NA's   :1
> summary.data.frame(Chr2TajiD.txt)
      all                HI                 LOW                MI
 Min.   :-2.8140   Min.   :-2.572004   Min.   :-2.6431   Min.   :-2.6741
 1st Qu.:-1.5083   1st Qu.:-0.852688   1st Qu.:-1.0568   1st Qu.:-1.1072
 Median :-0.9533   Median :-0.019460   Median :-0.4409   Median :-0.5075
 Mean   :-0.7653   Mean   : 0.001812   Mean   :-0.3375   Mean   :-0.4012
 3rd Qu.:-0.2282   3rd Qu.: 0.756601   3rd Qu.: 0.2513   3rd Qu.: 0.1784
 Max.   : 4.4483   Max.   : 3.659970   Max.   : 3.6552   Max.   : 3.4968
> summary.data.frame(Chr3TajiD.txt)
      all                HI                LOW                MI
 Min.   :-2.7906   Min.   :-2.68684   Min.   :-2.6494   Min.   :-2.6702
 1st Qu.:-1.5222   1st Qu.:-0.72652   1st Qu.:-1.1133   1st Qu.:-1.1024
 Median :-0.9528   Median : 0.05482   Median :-0.4825   Median :-0.4916
 Mean   :-0.7708   Mean   : 0.07815   Mean   :-0.3819   Mean   :-0.3843
 3rd Qu.:-0.1973   3rd Qu.: 0.79716   3rd Qu.: 0.2231   3rd Qu.: 0.2149
 Max.   : 3.9950   Max.   : 3.87120   Max.   : 3.7922   Max.   : 3.4765
> summary.data.frame(Chr4TajiD.txt)
      all                HI                 LOW                MI
 Min.   :-2.6994   Min.   :-2.550355   Min.   :-2.6602   Min.   :-2.6641
 1st Qu.:-1.5029   1st Qu.:-0.837174   1st Qu.:-1.1207   1st Qu.:-1.0363
 Median :-0.9386   Median :-0.002372   Median :-0.5089   Median :-0.4407
 Mean   :-0.7291   Mean   : 0.026764   Mean   :-0.3740   Mean   :-0.3053
 3rd Qu.:-0.1458   3rd Qu.: 0.787830   3rd Qu.: 0.2535   3rd Qu.: 0.3072
 Max.   : 4.2489   Max.   : 3.673539   Max.   : 3.6682   Max.   : 3.6864
> summary.data.frame(Chr5TajiD.txt)
      all                HI                LOW                MI
 Min.   :-2.8191   Min.   :-2.57128   Min.   :-2.6022   Min.   :-2.6541
 1st Qu.:-1.4746   1st Qu.:-0.79838   1st Qu.:-1.0316   1st Qu.:-1.0775
 Median :-0.8559   Median : 0.07804   Median :-0.3674   Median :-0.4273
 Mean   :-0.6643   Mean   : 0.10662   Mean   :-0.2441   Mean   :-0.3041
 3rd Qu.:-0.0635   3rd Qu.: 0.90451   3rd Qu.: 0.4089   3rd Qu.: 0.3347
 Max.   : 4.0332   Max.   : 3.69245   Max.   : 3.8514   Max.   : 3.6716

"""

HI = open('HI.txt.thetasWindow.gz.pestPG','r')
LO = open('LOW.txt.thetasWindow.gz.pestPG','r')
hi_out_b = open('HI_BalancingSites15.txt','w')
hi_out_s = open('HI_SelelectiveSweepSites15.txt','w')
Low_out_b = open('LOW_BalancingSites15.txt','w')
Low_out_s = open('LOW_SelelectiveSweepSites15.txt','w')

readhi = csv.reader(HI,delimiter='\t')
readlow = csv.reader(LO,delimiter='\t')

hi_out_b_writer = csv.writer(hi_out_b, delimiter = '\t')
hi_out_s_writer = csv.writer(hi_out_s, delimiter = '\t')
Low_out_b_writer = csv.writer(Low_out_b, delimiter = '\t')
Low_out_s_writer = csv.writer(Low_out_s, delimiter = '\t')

next(readhi, None)
next(readlow,None)

list_sl = []
list_bl = []
list_s = []
list_b = []

def getselectedsitesl(input):
    ##(indexStart,indexStop)(firstPos_withData,lastPos_withData)(WinStart,WinStop)	Chr	WinCenter	tW	tP	tF	tH	tL	Tajima	fuf	fud	fayh	zeng	nSites
    for row in input:
        if row[1] == 'Chr1':
            if float(row[8]) >= float(0.3042*1.5):
                list_bl.append(row)
            elif float(row[8]) <= float(-1.0785*1.5):
                list_sl.append(row)
            else:
                continue
        if row[1] == 'Chr2':
            if float(row[8]) >= float(0.2513*1.5):
                list_bl.append(row)
            elif float(row[8]) <= float(-1.0568*1.5):
                list_sl.append(row)
            else:
                continue
        if row[1] == 'Chr3':
            if float(row[8]) >= float(0.2231*1.5):
                list_bl.append(row)
            elif float(row[8]) <= float(-1.1133*1.5):
                list_sl.append(row)
            else:
                continue
        if row[1] == 'Chr4':
            if float(row[8]) >= float(0.2535*1.5):
                list_bl.append(row)
            elif float(row[8]) <= float(-1.1207*1.5):
                list_sl.append(row)
            else:
                continue
        if row[1] == 'Chr5':
            if float(row[8]) >= float(0.4089*1.5):
                list_bl.append(row)
            elif float(row[8]) <= float(-1.0316*1.5):
                list_sl.append(row)
            else:
                continue
    for i in list_bl:
        Low_out_b_writer.writerow(i)
    for f in list_sl:
        Low_out_s_writer.writerow(f)

def getselectedsites(input):
    ##(indexStart,indexStop)(firstPos_withData,lastPos_withData)(WinStart,WinStop)	Chr	WinCenter	tW	tP	tF	tH	tL	Tajima	fuf	fud	fayh	zeng	nSites
    for row in input:
        if row[1] == 'Chr1':
            if float(row[8]) >= float(0.814820*1.5):
                list_b.append(row)
            elif float(row[8]) <= float(-0.774959*1.5):
                list_s.append(row)
            else:
                continue
        elif row[1] == 'Chr2':
            if float(row[8]) >= float(0.756601*1.5):
                list_b.append(row)
            elif float(row[8]) <= float(-0.852688*1.5):
                list_s.append(row)
            else:
                continue
        elif row[1] == 'Chr3':
            if float(row[8]) >= float(0.79716*1.5):
                list_b.append(row)
            elif float(row[8]) <= float(-0.72652*1.5):
                list_s.append(row)
            else:
                continue
        elif row[1] == 'Chr4':
            if float(row[8]) >= float(0.787830*1.5):
                list_b.append(row)
            elif float(row[8]) <= float(-0.837174*1.5):
                list_s.append(row)
            else:
                continue
        elif row[1] == 'Chr5':
            if float(row[8]) >= float(0.90451*1.5):
                list_b.append(row)
            elif float(row[8]) <= float(-0.79838*1.5):
                list_s.append(row)
            else:
                continue
    for i in list_b:
        hi_out_b_writer.writerow(i)
    for f in list_s:
        hi_out_s_writer.writerow(f)


getselectedsites(readhi)
getselectedsitesl(readlow)

HI.close()
LO.close()
hi_out_b.close()
hi_out_s.close()
Low_out_b.close()
Low_out_s.close()
