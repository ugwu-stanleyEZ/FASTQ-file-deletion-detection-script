#now the visuals for my finding on the cftr child fastq file
#ill start by loading the core data visualization packages

library(tidyverse)
library(ggplot2)

#set the plot width and heigth (in inches)
options(repr.plot.width = 6, repr.plot.height =4)

#now ill add my cftr_child_pipline_results.csv file in R
results_data<- read_csv("cftr_child_pipeline_results.csv")

#next ill build a bar chart around it using ggplot2's geom_bar
ggplot(
    results_data, aes(x= Clinical_Diagnosis, fill = Clinical_Diagnosis  ))+
    geom_bar(width=0.5, color="#2c3e50",  size=0.8)+ 
    theme_minimal(base_size =14)+   
    #ill add labels
    labs(
        title = "CFTR Screening Variant Distribution", 
        subtitle ="Analysis of Child Patient Sequencing Pipeline Output",
        x = "Clinical Classification Summary",
        y = "Total Sequence Read Count",
        fill = "Diagnostic Status"
    )+
    theme(
        plot.title = element_text(face="bold", color="#1a252f", size=16),
        plot.subtitle = element_text(color="#7f8c8d", margin=margin(b=15)),
        axis.title= element_text(face="bold", color="#2c3e50"),
        panel.grid.minor=element_blank(),
        legend.position = "none"
    )
