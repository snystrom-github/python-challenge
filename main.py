import os
import csv

#Set variables to store data
totalvotes = 0
maxvotes = 0
candidates = {}
winner = ("")

#Set path to csv file
csvfile = "election_data.csv"
with open(csvfile, "r") as file:
  
