#!/usr/bin/env python
# coding: utf-8

# In[2]:


#this python scrypt parses through a FASTQ file to detect low quality and deleted bases in a squence
#And prints its output as a CSV file

import csv

with open("child.fastq", "r") as f:
    #will create variable with lines and use the .readlines() method to read the entire txt file, which will also turn the file 
    #into python list of text strings,   
    lines = f.readlines()

#open a clean csv file to write our structured results, file name will be CFTR (cystric fibrosis transmembrane conductance regulator)
with open ("cftr_child_pipeline_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Read_ID" , "Sequence", "QC_Status", "Clinical_Diagnosis" ])  

    #now our for loop for scaning/parsing through fastq files to dettect low quality or deletion
    for i in range (0, len(lines ), 4):
        header = lines[i].strip()
        sequence = lines[i+1].strip()
        plus = lines[i+2].strip()
        quality = lines[i+3].strip()

        #now our if conditional statements for what we want to get writtin inside our csv file
        if "!" in quality:
            writer.writerow([header, sequence, "Fail", "Not Analyzed"])
        elif "-" in sequence:
            writer.writerow([header, sequence, "Pass", "Mutation Detected"])
        else:
            writer.writerow([header, sequence, "Pass", "Normal"])

#now we print it
print("Data Export Complete! 'cftr_child_pipeline.csv' has been created")




# 
# 
