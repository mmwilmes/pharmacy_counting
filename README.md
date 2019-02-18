# Pharmacy counting challenge of the Insight Data Engineering program
### Solution by Madlen Wilmes

## Problem description

Efficiently process a large data file that provides the following information:

id: prescriber id<br>
*Prescriber_last*: Last name of physician that prescribed the medication<br>
*prescriber_first_name*: First name of physician that prescribed the medication<br>
*drug_name*: Name of the prescribed drug<br>
*drug_cost*: Cost of the prescription<br>

Special request: Use basic Python data structures, no external libraries, implement proper data engineering standards

**Example input file:**

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost<br>
1000000001,Smith,James,AMBIEN,100<br>
1000000002,Garcia,Maria,AMBIEN,200<br>
1000000003,Johnson,James,CHLORPROMAZINE,1000<br>
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000<br>
1000000005,Smith,David,BENZTROPINE MESYLATE,1500

Output the results as comma-separated file with the following information:

*drug_name*: the exact drug name as shown in the input dataset<br>
*num_prescriber*: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names<br>
*total_cost*: total cost of the drug across all prescribers

**Example output:**

drug_name,num_prescriber,total_cost<br>
CHLORPROMAZINE,2,3000<br>
BENZTROPINE MESYLATE,1,1500<br>
AMBIEN,2,300

## Description of solution

- read in comma separated file using csv library
- set up a dictionary for efficient data storage, drug name as keys
- if drug not yet in dictionary, initiate a list with two elements -> pharm{"drug":[{(last, first)}, number]
- first element of list is an empty set
- second element of list is a float
- within dictionary (for each drug) record tuple with prescriber first and last name within set, and add cost of that prescription to specified drug
- sort dict items (i.e. drugs) per cost (descending) and drug name (ascending), using a lambda function
- write all dict items to file, format cost with no decimals (not optimal for financial data, but required to pass insight test suite)

** Please note Pharmacy_counting_codedev.ipynb for more details on data exploration and successive development of code**