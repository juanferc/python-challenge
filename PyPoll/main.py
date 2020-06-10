import os
import csv

def voting_data():
    filepath = "election_data.csv"
    with open(filepath) as csvfile:
        #Define csv reader and separates the strings by comma
        csvreader = csv.reader(csvfile,delimiter = ",")
        csv_header = next(csvreader)
        total_votes = 0
        Khan = 0
        Correy = 0
        Li = 0
        Otooley = 0
        
        for row in csvreader:
            total_votes += 1
            
            if (row[2]) == "Khan":
                Khan += 1
            elif (row[2]) == "Correy":
                Correy += 1
            elif (row[2]) == "Li":
                Li += 1
            elif (row[2]) == "O'Tooley":
                Otooley += 1
        
        per_khan = Khan/total_votes
        new_per_khan = "{:.3%}".format(per_khan)
        per_correy = Correy/total_votes
        new_per_correy = "{:.3%}".format(per_correy)
        per_li = Li/total_votes
        new_per_li =  "{:.3%}".format(per_li)
        per_otooley = Otooley/total_votes
        new_per_otooley =  "{:.3%}".format(per_otooley)


        print("Election Results")
        print("-------------------------")
        print("Total Votes: " + str(total_votes))
        print("-------------------------")
        print("Khan: " + str(new_per_khan) + " " + "(" + str(Khan) + ")")
        print("Correy: " + str(new_per_correy) + " " + "(" + str(Correy) + ")")
        print("Li: " + str(new_per_li) + " " + "(" + str(Li) + ")")
        print("Otooley: " + str(new_per_otooley) + " " + "(" + str(Otooley) + ")")
        print("-------------------------")
        print("Winner: Khan")
        print("-------------------------")

        new_file_path = "results.txt"

        file1 = open(new_file_path,'w')
        file1.write("Election Results\n")
        file1.write("-------------------------\n")
        file1.write("Total Votes: " + str(total_votes) + "\n")
        file1.write("-------------------------\n")
        file1.write("Khan: " + str(new_per_khan) + " " + "(" + str(Khan) + ")" + "\n")
        file1.write("Correy: " + str(new_per_correy) + " " + "(" + str(Correy) + ")" + "\n")
        file1.write("Li: " + str(new_per_li) + " " + "(" + str(Li) + ")" + "\n")
        file1.write("Otooley: " + str(new_per_otooley) + " " + "(" + str(Otooley) + ")" + "\n")
        file1.write("-------------------------\n")
        file1.write("Winner: Khan\n")
        file1.write("-------------------------\n")

voting_data()

