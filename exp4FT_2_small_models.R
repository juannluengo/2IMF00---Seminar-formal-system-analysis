suppressPackageStartupMessages(library("dplyr"))


setwd(file.path(getwd(),"metasmallFT1"))

meta=read.csv2("fitness_full.csv",dec=".")
meta_group=meta %>% group_by(Name) %>% summarise(n = max(Epoch))
meta_group=meta_group%>%filter(n>0)
png("../fig2_FTsmallModels.png")
plot(ecdf(meta_group$n),
     main="",
     xlab="Number of Epochs [n]", cex.lab=1.8, cex.axis=1.8,cex.main=1.8,cex.sub=1.8)
dev.off()
print("Plot generated")
