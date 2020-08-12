fname=input("enter file name")
fopen=open(fname)
dic=dict()
for line in fopen:
  words=line.split()
  for word in words:
    dic[word]=dic.get(word,0)+1
highestcount=0
highestword=None
for k,v in dic.items():
  if v>highestcount:
    highestcount=v
    highestword=k
  
