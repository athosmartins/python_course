fname = input("Enter file name: ")
fh = open(fname,'r')
counts = {}

for lines in fh :
    if lines.startswith('From ') :
        sline = lines.split()
        sender = sline[1]
        counts[sender] = counts.get(sender,0) + 1

bigcount = None
bigsender = None
for sender,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigsender = sender

print(bigsender,bigcount)
