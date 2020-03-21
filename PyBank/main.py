import os 
import csv 

csv_path = os.path.join("Resources","budget_data.csv")

with open(csv_path) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=',')

    firstRow = next(budgetreader)

    dates = []
    changes = []
    total = 0 
    totalmonths = 0 
    profit_loss= 0
    prevbudget = 0 

    for row in budgetreader:
        
        total += int(row[1])
        
        change = int(row[1]) - prevbudget
        prevbudget = int(row[1])
        changes.append(change)

        totalmonths += 1
        
        dates.append(row[0]) 

greatest_increase = max(changes)
greatest_decrease = min(changes)
best_index = changes.index(greatest_increase)
worst_index = changes.index(greatest_decrease)
best_date = dates[best_index]
worst_date = dates[worst_index]

avg_change = sum(changes)/len(changes)


###################################

print("FINANCIAL ANALYSIS")
print("###################################")
print(f'Total Months: {totalmonths}')
print(f'Total:  ${total}')
print(f'Average Change: ${round(avg_change, 2)}')
print(f'Best Day: {best_date} (${greatest_increase})')
print(f'Worst Day: {worst_date} (${greatest_decrease})')
print("####################################")

####################################

output = open("PyBank.txt", "w")

line1= str("FINANCIAL ANALYSIS")
line2= str("###################################")
line3= str(f'Total Months: {totalmonths}')
line4= str(f'Total:  ${total}')
line5= str(f'Average Change: ${round(avg_change, 2)}')
line6= str(f'Best Day: {best_date} (${greatest_increase})')
line7= str(f'Worst Day: {worst_date} (${greatest_decrease})')
line8= str("####################################")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8))
