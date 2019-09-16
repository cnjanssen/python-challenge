import os
import csv

# path to file to be read
cereal_csv_path = os.path.join("..", "Resources", "election_data.csv")
#total number of votes
total = 0
#variables for the count of each one
count_khan = 0 
count_correy = 0 
count_li = 0
count_oTooley = 0 

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber
        #if float(row[7]) >= 5:
        total +=1

        if (row[2] == 'Khan'):
            count_khan +=1

        if (row[2] == 'Correy'):
            count_correy +=1

        if (row[2] == 'Li'):
            count_li +=1

        if (row[2] == "O'Tooley"):
            count_oTooley +=1


def print_results():
    print("Election Results:")
    print (f"total number of votes is {str(total)}")
    print("-----------------------------------------")
    print(f"Khan had {total_k} % and {count_khan} votes")
    print(f"Correy had {total_c} % and {count_correy} votes")
    print(f"Li had {total_l} % and {count_li} votes")
    print(f"O'Tooley had {total_o} % and {count_oTooley} votes")
    print("AND THE WINNER IS......................")



total_k = 100 * 1/(total / count_khan) 
total_c = 100 * 1/(total / count_correy)
total_l = 100 * 1/(total / count_li)
total_o = 100 * 1/(total / count_oTooley)

percents = [total_k, total_c, total_l, total_o]
#candidates = ["Khan", ]
can_per = {total_k: "Khan" , total_c: "Correy", total_l  : "Li",  total_o :"O'Tooley" } 

pop_win = max(percents)

winner = can_per[pop_win]



print(f"BEGIN")
print_results()
print (f"The candidate with the most popular vote had {pop_win} PERCENT and is {winner}")
print(f"END")


#writing output to .txt file

#declare variable f to open a file and the argument w to write the file and the plus sign to create it
#if the file does not exist, "+" means it will be made
f = open("pypoll_output.txt", "w+")
f.write("Election Results\n")
f.write("----------------\n")
f.write("Total Votes " +str(total) +"\n")

for cand in can_per:
    print(cand)
    
    #csvwriter.writerow([can_per[cand], cand * total, cand])
    row = str(can_per[cand]) + " : " +str(cand) + " % " +"(" +str(cand*total) +")"
    f.write(row +"\n")
    
f.write("The winner is " + str(winner))


# Specify the file to write to
output_path = os.path.join(".", ".", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(['Candidate', 'NUMBER', 'Percentages'])

    #write all necessary candidate percentages
    for cand in can_per:
        print(cand)
        csvwriter.writerow([can_per[cand], cand * total, cand])
        #print (f"The candidate with the most popular vote had {pop_win} PERCENT and is {winner}")
        #csvwriter.writerow([cand, int(can_per[cand]) * total, int(can_per[cand]])
        
    #write line break
    csvwriter.writerow(["-----", "------", "------"])
    
    #write winner row(last ROW)
    win_str = str(pop_win) + " %"
    csvwriter.writerow(["The WINNNER", win_str, winner])
