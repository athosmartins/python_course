fname = input("Enter file name: ")
fh = open(fname,'r')
count = 0

for line in fh :
    if line.startswith('From ') :
        sline = line.split()
        e = sline[1]
        print(e)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
