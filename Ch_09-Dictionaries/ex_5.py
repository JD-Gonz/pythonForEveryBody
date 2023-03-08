# Exercise 5: This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

emails = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        email = line.split()[1].split('@')[1]
        emails[email] = emails.get(email, 0) + 1
print(emails)