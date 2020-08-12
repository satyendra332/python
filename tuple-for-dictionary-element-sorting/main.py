fna=input("please enter the name of file:")
if len(fna) < 1 : fna = "romeo.txt"
fop=open(fna)
di=dict()
wo=[]
w=[]
lst=[]
t=tuple()
for line in fop:
    if 'From' not in line:
        continue
    words=line.split()
    if len(words)>4:
        wo.append(words[5])
for i in wo:
    w.append(i[:2])
for n in w:
    di[n]=di.get(n,0)+1
for k,v in di.items():
    t=(k,v)
    lst.append(t)

lst=sorted(lst)

for v,k in lst:
    print(v,k)
