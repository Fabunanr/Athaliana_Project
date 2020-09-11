## Boxplots TE_Superfamily
High_TE <- ggplot(TE_ForR, aes(x=TE_Superfamily, y = Group1_high, fill = Class)) + geom_boxplot() + ylim(0,12) + theme_classic() + labs(x = ' ', y = 'TE 
counts')

Low_TE <- ggplot(TE_ForR, aes(x=TE_Superfamily, y = Group2_low, fill = Class)) + geom_boxplot() + ylim(0,12) + theme_classic() + labs(x = 'TE Superfamily', y = 'TE counts')

## Commands for  Class I graphs
ClassI_TESuperfamily_boxplot <- ggplot(rs_ci_2, aes(x = TE_Superfamily, y = value, color = variable)) + geom_boxplot() + theme_classic() + labs(y = '',x = 'TE Superfamily', title = 'Class I Transposable element superfamilies', color = 'Elevation group') + scale_color_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP'))

ClassI_BoxPlot_gg <- ggplot(rs_ci, aes(x=variable, y = value, color = variable)) + geom_boxplot() + theme_classic() + labs(y = 'Counts',x = 'Elevation group',title = 'Class I Transposable elements') + guides(color=F) + scale_color_manual(values = c('steelblue3','orange1')) + guides(color = F) + scale_x_discrete(labels = c('HEP','LEP'))

DNA_En_spm_boxplot <- ggplot(rs_DNA_En_spm, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts', title = 'DNA En/Spm families', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))

DNA_Harbinger_boxplot <- ggplot(rs_DNA_Harbinger, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '',title = 'DNA Harbinger families', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))
 
DNA_Pogo_boxplot <- ggplot(rs_DNA_Pogo, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '',title = 'DNA Pogo families', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1)) 
 
DNA_boxplot <- ggplot(rs_DNA, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts',title = 'DNA families', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1))  + guides(fill = F)
  
DNA_Mariner_boxplot <- ggplot(rs_DNA_Mariner, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '',title = 'DNA Mariner families', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1))  + guides(fill = F)

DNA_Hat_boxplot <- ggplot(rs_DNA_Hat, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts',title = 'DNA Hat families', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1))  + guides(fill = F)

RC_Helitron_boxplot <- ggplot(rs_RC_helitron, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '',title = 'RC/Helitron families', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1))  + guides(fill = F)

grid.arrange(ClassI_BoxPlot_gg,ClassI_TESuperfamily_boxplot, DNA_En_spm_boxplot, DNA_Harbinger_boxplot, DNA_Pogo_boxplot,DNA_boxplot,DNA_Mariner_boxplot, DNA_Hat_boxplot, RC_Helitron_barchart,DNA_MuDr_boxplot, ncol=2, layout_matrix = lay)

lay <- rbind(c(1,1,2,2,2,2),
            c(1,1,2,2,2,2),
            c(3,3,3,4,5,6),
            c(7,7,7,8,8,8),
            c(9,9,9,9,9,9),
            c(9,9,9,9,9,9),
            c(10,10,10,10,10,10),
            c(10,10,10,10,10,10))
            
grid.arrange(ClassI_BoxPlot_gg,ClassI_TESuperfamily_boxplot, DNA_En_spm_boxplot, DNA_Mariner_boxplot, DNA_Harbinger_boxplot, DNA_Pogo_boxplot,DNA_boxplot, DNA_Hat_boxplot, RC_Helitron_boxplot,DNA_MuDr_boxplot, ncol=2, layout_matrix = lay)

## Commands for Class II Graphs
ClassII_BoxPlot_gg <- ggplot(rs_ci, aes(x = variable, y = value, color = variable)) + geom_boxplot() + theme_classic() + labs(y = 'Counts',x = 'Elevation group',title = 'Class II Transposable elements') + guides(color=F) + scale_color_manual(values = c('steelblue3','orange1')) + guides(color = F) + scale_x_discrete(labels = c('HEP','LEP'))

ClassII_TESuperfamily_BoxPlot <- ggplot(rs_cii_2, aes(x = TE_Superfamily, y = value, color = variable)) + geom_boxplot() + theme_classic() + labs(y = '',x = 'TE Superfamily', title = 'Class II Transposable element superfamilies', color = 'Elevation group') + scale_color_manual(values =c('steelblue3','orange1'), labels = c('HEP','LEP'))

SINE_boxplot <- ggplot(rs_SINE, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '', title = 'SINE', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))

RathE1_boxplot <- ggplot(rs_RathE1_cons, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = '', title = 'RathE1_cons', x = '', fill = 'Elevation group') + scale_fill_manual(values =c('steelblue3','orange1'),labels = c('HEP','LEP')) + theme(axis.text.x=element_text(angle=90, hjust=1))

LINE_boxplot <- ggplot(rs_line, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts', title = 'LINE', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))

LTR_Gypsy_boxplot <- ggplot(rs_LTR_gypsy, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts', title = 'LTR/GYPSY', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))

LTR_COPIA_boxplot <- ggplot(rs_LTR_copia, aes(x=TE_Family,y=value,fill=variable)) + geom_bar(stat='identity', position = 'dodge') + theme_classic() + labs(y = 'Counts', title = 'LTR/COPIA', x = '') + scale_fill_manual(values =c('steelblue3','orange1')) + guides(fill = F) + theme(axis.text.x=element_text(angle=90, hjust=1))

lay <- rbind(c(1,1,2,2,2,2),
            c(3,3,3,3,4,5),
            c(6,6,6,6,6,6),
            c(7,7,7,7,7,7))
            
grid.arrange(ClassII_BoxPlot_gg,ClassII_TESuperfamily_BoxPlot, LINE_boxplot,SINE_boxplot,RathE1_boxplot,LTR_COPIA_boxplot,LTR_Gypsy_boxplot,layout_matrix = lay)

> wilcox.test(ClassI$Group1_high,ClassI$Group2_low)

	Wilcoxon rank sum test with continuity correction

data:  ClassI$Group1_high and ClassI$Group2_low
W = 2111, p-value = 0.6108
alternative hypothesis: true location shift is not equal to 0

> classi_anova <- aov(value ~ variable + TE_Superfamily ,data = rs_ci_2)
> summary(classi_anova)
                Df Sum Sq Mean Sq F value Pr(>F)
variable         1   22.2   22.18   1.716  0.193
TE_Superfamily   7  110.1   15.72   1.217  0.299
Residuals      118 1525.2   12.93               
37 observations deleted due to missingness

> wilcox.test(ClassII$Group1_high,ClassII$Group2_low)

	Wilcoxon rank sum test with continuity correction

data:  ClassII$Group1_high and ClassII$Group2_low
W = 1288.5, p-value = 0.01991
alternative hypothesis: true location shift is not equal to 0

> classii_anova <- aov(value ~ variable + TE_Superfamily ,data = rs_cii_2)
> summary(classii_anova)
               Df Sum Sq Mean Sq F value  Pr(>F)   
variable        1  26.15   26.16   8.719 0.00407 **
TE_Superfamily  4  47.28   11.82   3.941 0.00554 **
Residuals      85 254.98    3.00                   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
33 observations deleted due to missingness

> wilcox.test(Line$Group1_high, Line$Group2_low)

	Wilcoxon rank sum test with continuity correction

data:  Line$Group1_high and Line$Group2_low
W = 65, p-value = 0.02954
alternative hypothesis: true location shift is not equal to 0

> wilcox.test(LTR_Copia$Group1_high, LTR_Copia$Group2_low)

	Wilcoxon rank sum test with continuity correction

data:  LTR_Copia$Group1_high and LTR_Copia$Group2_low
W = 363.5, p-value = 0.0967
alternative hypothesis: true location shift is not equal to 0

> wilcox.test(LTR_gypsy$Group1_high, LTR_gypsy$Group2_low)

	Wilcoxon rank sum test with continuity correction

data:  LTR_gypsy$Group1_high and LTR_gypsy$Group2_low
W = 64.5, p-value = 0.2748
alternative hypothesis: true location shift is not equal to 0