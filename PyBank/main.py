import os
import csv
def records_analysis():
    #Set a variable with the file's path
    filepath = "budget_data.csv"
    #Open the csv file
    with open(filepath) as csvfile:
        #Define csv reader and separates the strings by comma
        csvreader = csv.reader(csvfile,delimiter = ",")
        csv_header = next(csvreader)
        net_amount_PL = 0
        averge_change = []
        prevPL = 0
        mth_array = []
        p_array = []
        for row in csvreader:
            p_array.append(int(row[1]))
            mth_array.append(str(row[0]))
            net_amount_PL += int(row[1])
            if prevPL == 0:
                prevPL = int(row[1])
            else:
                averge_change.append(int(row[1]) - prevPL)
                prevPL = int(row[1])
        most_final = 0
        for i in range(len(p_array)-1):
            maximum = int(p_array[i+1])-int(p_array[i])
            if maximum > most_final:
                most_final = maximum
                monthlymax = mth_array[i+1]
        least_final = 0
        for i in range(len(p_array)-1):
            minimum = int(p_array[i+1])-int(p_array[i])
            if minimum < least_final:
                least_final = minimum
                monthlymin = mth_array[i+1]
        for each in range(0,len(averge_change)):
            net_amount_Pl = net_amount_PL + averge_change[each]
        
        print("Financial Analysis")
        print("----------------------")
        print("Total months: " + str(len(averge_change)+1))
        print("Total: $" + str(net_amount_PL))
        print("Average Change: $" + str(round(sum(averge_change)/len(averge_change),2)))
        print("Greatest Increase in Profits: " + str(monthlymax) + " " +  "($" + str(most_final) + ")")
        print("Greatest Decrease in Profits: " + str(monthlymin) + " " +  "($" + str(least_final) + ")")

        new_file_path = "analysis.txt"

        #Open the file using "write" mode
        file1 = open(new_file_path,'w')
        file1.write("Financial Analysis\n")
        file1.write("----------------------\n")
        file1.write("Total months: " + str(len(averge_change)+1) + "\n")
        file1.write(("Total: $" + str(net_amount_PL) + "\n"))
        file1.write("Average Change: $" + str(round(sum(averge_change)/len(averge_change),2)) + "\n")
        file1.write("Greatest Increase in Profits: " + str(monthlymax) + " " +  "($" + str(most_final) + ")" + "\n") 
        file1.write("Greatest Decrease in Profits: " + str(monthlymin) + " " +  "($" + str(least_final) + ")" + "\n")

    
      

       
records_analysis()

        



        



