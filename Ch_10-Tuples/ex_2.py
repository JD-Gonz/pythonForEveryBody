# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string 
# and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.

hours = dict()
fh = open('../mbox-short.txt')
for line in fh :
    if line.startswith('From ') :
        hour = line.split()[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1
for k,v in sorted(hours.items()) :
    print(k,v)