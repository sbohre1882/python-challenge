import os
import csv

mcount = 0
total = 0
PreValue = 0
Diff = 0
Max = 0
Min = 0
total_diff=0

with open('budget_data.csv', newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     #for row in csvfile:
         #print(row)
     for i in csvreader:
         month = i[0]
         revenue = i[1]
         rev = int(revenue)
         Diff =  rev - PreValue
         
         if Max < Diff:
            Max = Diff
            DiffMaxDate = month
         
         if Min > Diff:
            Min = Diff
            DiffMinDate = month

         PreValue = rev   
         mcount = mcount + 1
         total+= int(rev)
         total_diff+=int(Diff) 
ave_diff=round(total_diff/mcount,2)
output=(
f'Total Months : {mcount}\n'
f'Total: $ {total}\n'
f'Average Change: ${ave_diff}\n'
f'Greatest Increase in Profits: {DiffMaxDate} : $ {Max}\n'
f'Greatest Decrease in Profits: {DiffMinDate} : $ {Min}\n'
)
print(output)

with open('output.txt', "w") as txt:
    txt.write(output)
