fna=input("please enter the name of file:")
fop=open(fna)
counts=dict()
wo=[]
for line in fop:
    if 'From' not in line:
        continue
    words=line.split()
    if len(words)>2:
        wo.append(words[1])
for w in wo:
    counts[w]=counts.get(w,0)+1
highcount=0
highword=0
for word,count in counts.items():
    if word==0 or highcount<count:
        highcount=count
        highword=word
print(highword,highcount)
