#Add our dependancies
import csv
import os

#Assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read file
with open(file_to_load) as election_data:

    #To do: Read and analyze data
    #Read file object with reader function
    file_reader = csv.reader(election_data)

    #Print each row in CSV file
    for row in file_reader:
        print(row)
        