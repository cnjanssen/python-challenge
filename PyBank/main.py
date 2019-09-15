import os
import csv

#test 1

# path to file to be read
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
csv_path = os.path.join("..", "Resources", "budget_data.csv")


# The total number of months included in the dataset
total_months = 0
net_amt = 0 
amounts = []
months = []

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader)

    for row in csv_reader:
        # print(f" {row[0]} and value is {row[1]}")
        total_months +=1
        #print(f" At second column we have {row[1]}")
        net_amt = net_amt + int(row[1])
        months.append(row[0])
        amounts.append(row[1])

average = net_amt/total_months

#get greatest increase/decrease from list of all amounts
great_inc = max(amounts)
great_dec = min(amounts)

#get greatest increase/decrease INDEX from list of all amounts
index_great_inc = amounts.index(great_inc)
index_great_dec = amounts.index(great_dec)



#great_inc_month = months[]
print (f"There are {total_months} months")
print (f"There was {net_amt} Dollars  NET")
print (f"The AVERAGE net change was {average} Dollars AVERAGE PER Month")
print (f"The greast increase was {great_inc} and it happend at {months[index_great_inc]}  ")
print (f"The greast decrease was {great_dec} and it happend at {months[index_great_dec]} ")

big_month = str(great_inc+ " " +months[index_great_inc])
small_month = str(great_dec+ " " +months[index_great_dec])


#Writing output to CSV


# Specify the file to write to
output_path = os.path.join(".", ".", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(['Total Months', total_months])

    # Write the second row
    csvwriter.writerow(['NET Dollars', net_amt])

     # Write the third row
    csvwriter.writerow(['AVERAGE NET Dollars', average])

    # Write the fourth row
    csvwriter.writerow(['GREATEST INCREASE', big_month])

    # Write the fourth row
    csvwriter.writerow(['GREATEST DECREASE', small_month])