f=open("count_cases.txt")
c=f.read()
words=c.split()
a=[]
b=[]
i=0
count_lower=0
count_upper=0
while i<len(words):
    j=0
    while j<len(words[i]):
        if words[i][j].isupper():
            a.append(words[i][j])
            count_upper+=1
        elif words[i][j].islower():
            count_lower+=1
            b.append(words[i][j])
        j+=1
    i+=1
# print(a)
# print(b)
print(count_upper)
print(count_lower)