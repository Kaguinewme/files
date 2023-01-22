import os
print(os.path.getsize("filesize.txt"))

# file=open("filesize.txt")
# size=len(file.read())
# print(size)

file=open("filesize.txt")
print(file.read())
print(file.tell())
# i=0
# count=0
# while i<len(f):
#     count+=1
#     i+=1
# print(count)