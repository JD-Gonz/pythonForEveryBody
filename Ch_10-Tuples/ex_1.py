# Exercise 1: Revise a previous program as follows: 
# Read and parse the "From" lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary. 
# After all the data has been read, 
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

emails = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1
maxCom = sorted([(v, k) for k,v in emails.items()], reverse=True)[0]
print(maxCom[1], maxCom[0])