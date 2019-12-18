import csv

data = []
#Read CSV File
path = "budget_data.csv"
with open(path, 'r') as file:  
    next(file)
    months = sum(1 for line in csv.reader(file))
with open(path, 'r') as file:  
    next(file)
    total = 0
    for row in csv.reader(file):
        date = str(row[0])
        pnl = float(row[1])
        total += pnl
        data.append([date, pnl])

print("Total Months:  " , format(months))
print("Total :  " , '${:.2f}'.format(total))

#Write CSV File
path = "budget_data_returns.csv"
with open(path, 'w') as write_file:
    csv.writer(write_file).writerow(["Date" , "Return"])
    for i in range(months -1):
        today_row = data[i + 1]
        today_date = today_row[0]
        today_pnl = today_row[1]
        yest_row = data[i]
        yest_pnl = yest_row[1]
        change = today_pnl - yest_pnl
        csv.writer(write_file).writerow([today_date , change])

#Average Ret 
with open(path, 'r') as file:  
    next(file)
    total_change = 0
    for row in csv.reader(file):
        total_change += float(row[1])
        average_change = total_change / months
        
        
    
print("Total Months:  " , format(months))
print("Total :  " , '${:.2f}'.format(total))    
print("Average Change :  " , '${:.2f}'.format(average_change))
