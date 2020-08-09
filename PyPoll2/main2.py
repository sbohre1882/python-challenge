import csv
import os

votes = 0; winner = 0; total_candidates = 0
winnervotes = ["", 0]
candidateOptions = []
candidateVotes = {}


with open('election_data.csv') as text:
    reader = csv.DictReader(text)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidateOptions:  
            candidateOptions.append(row["Candidate"])
            candidateVotes[row["Candidate"]] = 1
        else:
            candidateVotes[row["Candidate"]] = candidateVotes[row["Candidate"]] + 1
    
    if (votes > winner):
        winnervotes[1] = candidateVotes
        winnervotes[0] = row["Candidate"]
    
    
    print("Election Results")
    print("<(-_-)>")
    print("Total Votes " + str(votes))
    print("<(-_-)>")
#results
    for candidate in candidateVotes:
        print(candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")") 
    
candidateVotes

winner = sorted(candidateVotes.items(),)

#results
print("<(-_-)>")
print("Winner: " + str(winner[1]))
print("<(-_-)>")

with open('output2.txt','w') as t:
    t.write('Election Results\n')
    t.write('------------\n')
    #t.write(candidate + "" + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")"+'\n')
    for candidate in candidateVotes:
        t.write(candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")" +'\n') 
        candidate_results = (candidate + " " + str(round(((candidateVotes[candidate]/votes)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")")
    t.write('The Winner Is: '+ str(winner[1])+'\n')
    t.write('Total Votes: '+ str(votes))



