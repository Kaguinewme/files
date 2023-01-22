#===============read no. of words================
# file=open("list.txt")
# print(len(file.read().split()))


file=open("list.txt")
file1=file.read()
file2=file1.split()
print(len(file2))