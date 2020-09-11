Chr1_SNPden_build <- ggplot_build(chr1_snpden_new)
Chr1_SNPden_df <- Chr1_SNPden_build[["data"]][[1]]

Chr3_SNPden_build <- ggplot_build(chr2_snpden_new)
Chr2_SNPden_df <- Chr2_SNPden_build[["data"]][[1]]

Chr3_SNPden_build <- ggplot_build(chr3_snpden_new)
Chr3_SNPden_df <- Chr3_SNPden_build[["data"]][[1]]

Chr4_SNPden_build <- ggplot_build(chr4_snpden_new)
Chr4_SNPden_df <- Chr4_SNPden_build[["data"]][[1]]

Chr5_SNPden_build <- ggplot_build(chr5_snpden_new)
Chr5_SNPden_df <- Chr5_SNPden_build[["data"]][[1]]

Chr1_MethLevel_build <- ggplot_build(Chr1_MethLevel_new)
Chr1_MethLevel_df <- Chr1_MethLevel_build[["data"]][[1]]

Chr2_MethLevel_build <- ggplot_build(Chr2_MethLevel_new)
Chr2_MethLevel_df <- Chr2_MethLevel_build[["data"]][[1]]

Chr3_MethLevel_build <- ggplot_build(Chr3_MethLevel_new)
Chr3_MethLevel_df <- Chr3_MethLevel_build[["data"]][[1]]

Chr4_MethLevel_build <- ggplot_build(Chr4_MethLevel_new)
Chr4_MethLevel_df <- Chr4_MethLevel_build[["data"]][[1]]

Chr5_MethLevel_build <- ggplot_build(Chr5_MethLevel_new)
Chr5_MethLevel_df <- Chr5_MethLevel_build[["data"]][[1]]

Chr1_tajd_build <- ggplot_build(chr1_tajd_new)
Chr1_tajd_df <- Chr1_tajd_build[["data"]][[1]]

Chr2_tajd_build <- ggplot_build(chr2_tajd_new)
Chr2_tajd_df <- Chr2_tajd_build[["data"]][[1]]

Chr3_tajd_build <- ggplot_build(chr3_tajd_new)
Chr3_tajd_df <- Chr3_tajd_build[["data"]][[1]]

Chr4_tajd_build <- ggplot_build(chr4_tajd_new)
Chr4_tajd_df <- Chr4_tajd_build[["data"]][[1]]

Chr5_tajd_build <- ggplot_build(chr5_tajd_new)
Chr5_tajd_df <- Chr5_tajd_build[["data"]][[1]]

Chr1_SNPden_df <- data.frame(Chr1_SNPden_df$group,rep("Chr1"),Chr1_SNPden_df$x,Chr1_SNPden_df$x,Chr1_SNPden_df$y)
Chr2_SNPden_df <- data.frame(Chr2_SNPden_df$group,rep("Chr2"),Chr2_SNPden_df$x,Chr2_SNPden_df$x,Chr2_SNPden_df$y)
Chr3_SNPden_df <- data.frame(Chr3_SNPden_df$group,rep("Chr3"),Chr3_SNPden_df$x,Chr3_SNPden_df$x,Chr3_SNPden_df$y)
Chr4_SNPden_df <- data.frame(Chr4_SNPden_df$group,rep("Chr4"),Chr4_SNPden_df$x,Chr4_SNPden_df$x,Chr4_SNPden_df$y)
Chr5_SNPden_df <- data.frame(Chr5_SNPden_df$group,rep("Chr5"),Chr5_SNPden_df$x,Chr5_SNPden_df$x,Chr5_SNPden_df$y)

Chr1_MethLevel_df <- data.frame(Chr1_MethLevel_df$group,rep("Chr1"),Chr1_MethLevel_df$x,Chr1_MethLevel_df$x,Chr1_MethLevel_df$y)
Chr2_MethLevel_df <- data.frame(Chr2_MethLevel_df$group,rep("Chr2"),Chr2_MethLevel_df$x,Chr2_MethLevel_df$x,Chr2_MethLevel_df$y)
Chr3_MethLevel_df <- data.frame(Chr3_MethLevel_df$group,rep("Chr3"),Chr3_MethLevel_df$x,Chr3_MethLevel_df$x,Chr3_MethLevel_df$y)
Chr4_MethLevel_df <- data.frame(Chr4_MethLevel_df$group,rep("Chr4"),Chr4_MethLevel_df$x,Chr4_MethLevel_df$x,Chr4_MethLevel_df$y)
Chr5_MethLevel_df <- data.frame(Chr5_MethLevel_df$group,rep("Chr5"),Chr5_MethLevel_df$x,Chr5_MethLevel_df$x,Chr5_MethLevel_df$y)

Chr1_tajd_df <- data.frame(Chr1_tajd_df$group,rep("Chr1"),Chr1_tajd_df$x,Chr1_tajd_df$x,Chr1_tajd_df$y)
Chr2_tajd_df <- data.frame(Chr2_tajd_df$group,rep("Chr2"),Chr2_tajd_df$x,Chr2_tajd_df$x,Chr2_tajd_df$y)
Chr3_tajd_df <- data.frame(Chr3_tajd_df$group,rep("Chr3"),Chr3_tajd_df$x,Chr3_tajd_df$x,Chr3_tajd_df$y)
Chr4_tajd_df <- data.frame(Chr4_tajd_df$group,rep("Chr4"),Chr4_tajd_df$x,Chr4_tajd_df$x,Chr4_tajd_df$y)
Chr5_tajd_df <- data.frame(Chr5_tajd_df$group,rep("Chr5"),Chr5_tajd_df$x,Chr5_tajd_df$x,Chr5_tajd_df$y)


thelist <- c('Chr1_SNPden_df','Chr2_SNPden_df','Chr3_SNPden_df','Chr4_SNPden_df','Chr5_SNPden_df')
listtt <- mget(thelist)

for (i in 1:length(listtt)){
  write.table(listtt[[i]],paste(names(listtt[i]),'.csv'),sep=',',quote=F,row.names=F,col.names = F)
}

Low_GFF_fixed <- AllLowGff
Low_GFF_fixed$V1 <- with(Low_GFF_fixed, factor(V1, levels=paste('Chr',c(1:5),sep=''),ordered = T))
plotted_lowgfffixed <- ggplot(Low_GFF_fixed) + geom_histogram(aes(x=V2),binwidth=100000) + facet_wrap(~V1,ncol=5)
Low_plottingdata <- ggplot_build(plotted_lowgfffixed)
df_low_plottingdata <- data.frame(Low_plottingdata[["data"]][[1]]$PANEL,Low_plottingdata[["data"]][[1]]$xmin,Low_plottingdata[["data"]][[1]]$xmax,Low_plottingdata[["data"]][[1]]$density)


High_GFF_fixed <- allhighgff
High_GFF_fixed$V1 <- with(High_GFF_fixed, factor(V1, levels=paste('Chr',c(1:5),sep=''),ordered = T))
plotted_Highgfffixed <- ggplot(High_GFF_fixed) + geom_histogram(aes(x=V2),binwidth=100000) + facet_wrap(~V1,ncol=5)
High_plottingdata <- ggplot_build(plotted_Highgfffixed)
df_High_plottingdata <- data.frame(High_plottingdata[["data"]][[1]]$PANEL,High_plottingdata[["data"]][[1]]$xmin,High_plottingdata[["data"]][[1]]$xmax,High_plottingdata[["data"]][[1]]$density)

write.table(df_low_plottingdata,'Low_TE_Density_circos.csv',quote=F,row.names = F,col.names = F)
write.table(df_High_plottingdata,'High_TE_Density_circos.csv',quote=F,row.names = F,col.names = F)
