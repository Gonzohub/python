import os 
import csv 

csv_path = os.path.join("Resources","election_data.csv")

with open(csv_path) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',')

    firstRow = next(election_reader)
    
    total_votes = 0 
    candidates = []
    num_votes = []

    for vote in election_reader:

        total_votes += 1 

        if vote[2] not in candidates:
            candidates.append(vote[2])
            num_votes.append(1)
        
        else:
            index = candidates.index(vote[2])
            num_votes[index] += 1 

windex = num_votes.index(max(num_votes))
Winner = candidates[windex]

####################################################################        
    
print("Election Results")
print("************************************")
print(f'Total Votes: {total_votes}')
print("************************************")
print(f'{candidates[0]}: {round((num_votes[0]/total_votes)*100)}.000% ({num_votes[0]})')
print(f'{candidates[1]}: {round((num_votes[1]/total_votes)*100)}.000% ({num_votes[1]})')
print(f'{candidates[2]}: {round((num_votes[2]/total_votes)*100)}.000% ({num_votes[2]})')
print(f'{candidates[3]}: {round((num_votes[3]/total_votes)*100)}.000% ({num_votes[3]})')
print("************************************")

print(f'Winner: {Winner}')

####################################################################
output = open("PyPoll.txt", "w")

line1= str("Election Results")
line2= str("************************************")
line3= str(f'Total Votes: {total_votes}')
line4= str("************************************")
line5= str(f'{candidates[0]}: {round((num_votes[0]/total_votes)*100)}.000% ({num_votes[0]})')
line6= str(f'{candidates[1]}: {round((num_votes[1]/total_votes)*100)}.000% ({num_votes[1]})')
line7= str(f'{candidates[2]}: {round((num_votes[2]/total_votes)*100)}.000% ({num_votes[2]})')
line8= str(f'{candidates[3]}: {round((num_votes[3]/total_votes)*100)}.000% ({num_votes[3]})')
line9= str("************************************")
line10= str(f'Winner: {Winner}')

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10))