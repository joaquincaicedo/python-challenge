import csv

path = "election_data.csv"
total_votes = 0
most_votes = 0
winner = 0
candidates = []

#Total Votes
with open(path, 'r') as file:  
    next(file)
    total_votes = sum(1 for line in csv.reader(file))
    print("Total Votes        :" , total_votes)

#Candidate List
with open(path, 'r') as file:  
    next(file)
    for row in csv.reader(file):
        candidate = str(row[2]) 
        if candidate not in candidates:
            candidates.append(candidate)
#Vote Count and Winner           
for name in candidates:
    vote = 0
    share = 0
    with open(path, 'r') as file:  
        next(file)
        for row in csv.reader(file):
            if name == str(row[2]):
                vote += 1
                share = vote / total_votes
                if vote > most_votes:
                    most_votes = vote
                    winner = name
        print("Candidate:  " , name    , "     ", "Votes:" , vote, "     ","Share:" ,    '{:.2%}'.format(share))

print("Winner is      :" , winner)