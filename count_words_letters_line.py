f=open("count_words_letters_line.txt")
f1=f.read()
f2=f1.split()
i=0
count_letters=0
while i<len(f2):
    j=0
    while j<len(f2[i]):
        count_letters+=1
        j+=1
    i+=1
print("no. of words:",len(f2))
print("no. of letters:",count_letters)
f.close()
f3=open("count_words_letters_line.txt")
f4=f3.readlines()
print("no. of lines:",len(f4))