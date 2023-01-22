f=open("vowel_consonant.txt")
f1=f.read()
f2=f1.split()
i=0
vowel=0
consonant=0
while i<len(f2):
    j=0
    while j<len(f2[i]):
        if f2[i][j]=="a" or "e" or "i" or "o" or "u":
            vowel+=1
        else:
            consonant+=1
        j+=1
    i+=1
print(vowel)
print(consonant)