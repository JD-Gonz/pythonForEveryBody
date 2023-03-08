# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come from each email address,
# and print the dictionary.

emails = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1
print(emails)