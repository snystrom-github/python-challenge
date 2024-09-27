#Import modules
import os
import csv

#Open the right csv file path
csv_file = 'budget_data.csv'

#Create lists
months = []
profits = []
profitchanges = []

#Read csv file
with open(csv_file, mode='r') as file:
  csvreader = csv.reader(file)
  next(csvreader)

  #Get data for months and profits
  for row in csv reader:
    months.append(row[0])
    profits.append(int(row[1]))

#Set functions
totalmonths = len(months)
totalprofits = sum(profits)

#Calcluate profit/loss changes
for i in range(1, len(profits)):
  change = profits[i] - profits[i - 1]
  profitchanges.append(change)

#Calculate average profit/loss changes
averagechange = sum(profitchanges / len(profitchanges)

#Calculate greatest increase/decrease and months
greatestincrease = max(profitchanges)
greatestdecrease = min(profitchanges)
increaseindex = profitchanges.index(greatestincrease) + 1
decreaseindex = profitchanges.index(greatestdecrease) + 1
greatestincreasemonth = months[increaseindex]
greatestdecreasemonth = months[decreaseindex]

#Print output
print("Financial Analysis")
print("----------------------------")
#Print total nmber of months included in the dataset
print(f"Total Months: {totalmonths}")
#Print the net total amount of Profit/Losses column over entire period                     
print(f"Total" ${totalprofits}")

#Print the changes in Profit/Losses colum over entire period and the average of those changes
print(f"Average Change: ${totalprofits}")

#Print the greatest increase in profits with date and amount over the entire period
print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")
#Print the greatest decrease in profits with date and amount over the entire period
print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease")



                     
