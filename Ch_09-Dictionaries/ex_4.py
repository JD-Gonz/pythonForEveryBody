# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop to find who has the most messages
# and print how many messages the person has.

emails = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1
maxCount = None
maxEmail = None
for email,count in emails.items() :
    if maxCount is None or maxCount < count :
        maxCount = count
        maxEmail = email
print(maxEmail, maxCount)