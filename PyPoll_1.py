import csv

dir(csv)

# Assign a variable for file to load and the path
file_to_load = 'Resources\election_results.csv'

#Open the file and read
election_data = open(file_to_load, 'r')

#Open the file and read
with open(file_to_load) as election_data:

    #To do: Perform analysis.
    print(election_data)

import csv
import os

#Assign a variable for file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the file and read
with open (file_to_load) as election_data:
    print(election_data)

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using open() function with w to write data to the file
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write 3 counties name
     txt_file.write("Counties in the election\n_____________________\nArapahoe\nDenver\nJefferson")



