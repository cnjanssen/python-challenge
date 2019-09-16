import os
import csv

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





#writing output to .txt file

#declare variable f to open a file and the argument w to write the file and the plus sign to create it
#if the file does not exist, "+" means it will be made
f = open("pybank_output.txt", "w+")

f.write("There are " +str(total_months) +" months\n")
f.write("There was " +str(net_amt) +" Dollars  NET\n")
f.write("The AVERAGE net change was " +str(average) +" Dollars AVERAGE PER Month\n")
f.write("The greast increase was " +str(great_inc) +" and it happend at " +str(months[index_great_inc]) +"\n")
f.write("The greast decrease was " +str(great_dec) +" and it happend at " +str(months[index_great_dec]) +"\n")
f.close()
