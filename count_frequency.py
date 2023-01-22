def word_frequency(file_name):
    file=open(file_name)
    f=file.read()
    f1=f.split()
    print(f1)
    i=0
    count=0
    while i<len(f1):
        if word==f1[i]:
            count+=1
        i+=1
    print(count)
word=input("enter word;")
word_frequency("count_frequency.txt")