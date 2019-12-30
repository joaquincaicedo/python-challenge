import csv

# Define Variables
data = []
total = 0
average_change = 0
max_dec = 0
min_dec = 0

#Read CSV File
path = "budget_data.csv"
with open(path, 'r') as file:  
    next(file)
    months = sum(1 for line in csv.reader(file))
with open(path, 'r') as file:  
    next(file)
    for row in csv.reader(file):
        date = str(row[0])
        pnl = float(row[1])
        total += pnl
        data.append([date, pnl])

#Write CSV File
path = "budget_data_returns.csv"
with open(path, 'w', newline = '' ) as write_file:
    csv.writer(write_file).writerow(["Date" , "Return"])
    for i in range(months - 1  ):
        today_row = data[i + 1]
        today_date = today_row[0]
        today_pnl = today_row[1]
        yest_row = data[i]
        yest_pnl = yest_row[1]
        change = today_pnl - yest_pnl
        csv.writer(write_file).writerow([today_date , change])

#Average Return 
with open(path, 'r') as file:  
    next(file)
    total_change = 0
    for row in csv.reader(file):
        total_change += float(row[1])
        average_change = total_change / (months - 1)
        
#Greatest Increase in Profits
with open(path, 'r') as file:  
    next(file)
    for row in csv.reader(file):
        if max_dec < float(row[1]):
            max_dec = float(row[1])
            month_max = row[0]
        
        
#Greatest Decrease in Profits
with open(path, 'r') as file:  
    next(file)
    for row in csv.reader(file):
        if min_dec > float(row[1]):
            min_dec = float(row[1])
            month_min = row[0]        
        

    
print("Total Months                 :  " , format(months))
print("Total                        :  " , '${:.2f}'.format(total))    
print("Average Change               :  " , '${:.2f}'.format(average_change))
print("Greatest Increase in Profits :  " , '${:.2f}'.format(max_dec) , "in" , month_max)
print("Greatest Decrease in Profits :  " , '${:.2f}'.format(min_dec) , "in" , month_min)
print("Check results in results.txt")


#Write Optimized Variables
with open ("results.txt", "w") as result_text:
    print("Total Months                 :  " , format(months) , file = result_text )
    print("Total                        :  " , '${:.2f}'.format(total), file = result_text)    
    print("Average Change               :  " , '${:.2f}'.format(average_change), file = result_text)
    print("Greatest Increase in Profits :  " , '${:.2f}'.format(max_dec) , "in" , month_max , file = result_text)
    print("Greatest Decrease in Profits :  " , '${:.2f}'.format(min_dec) , "in" , month_min , file = result_text)
    

