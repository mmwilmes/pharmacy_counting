
# coding: utf-8

# In[1]:


import csv
import sys


# In[9]:


# read pharmacy file into data structure
def read_pharma_file(infile):
    pharm = {}
    with open(infile, "r") as f:
    #with open("../input/data_trunc.txt", "r") as f:
        my_data = csv.DictReader(f)
        for line in my_data:
            drug = line["drug_name"]
            prescriber = tuple([line["prescriber_first_name"], line["prescriber_last_name"]])
            cost = float(line["drug_cost"])
            pharm[drug] = pharm.get(drug, [set(),0])
            pharm[drug][0].add(prescriber)
            pharm[drug][1] = pharm[drug][1] + cost
        return(pharm)


# In[10]:


def sort_pharmacy(pharm):
    sort_pharm = sorted(pharm.items(), key = lambda x: (-x[1][1],x[0]))
    return(sort_pharm)


# In[11]:


def write_outfile(sorted_pharm, outfile):
    with open(outfile,"w") as of:
        of.write("drug_name,num_prescriber,total_cost")
        for drug in sorted_pharm:
            of.write("\n{},{},{:.0f}".format(drug[0], len(drug[1][0]), drug[1][1],2))


# In[12]:


def pharmacy_counting(infile, outfile):
    pharm = read_pharma_file(infile)
    #pharm = process_pharma(my_data)
    sorted_pharm = sort_pharmacy(pharm)
    write_outfile(sorted_pharm, outfile)


# In[9]:


if __name__ == "__main__":
# read the arguments on the command line 
    infile = sys.argv[1]
    outfile = sys.argv[2]
# run pharmacy_counting
    pharmacy_counting(infile, outfile)

