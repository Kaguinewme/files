# file=open("longest_word.txt")
# file1=file.read()
# words=file1.split()
# print(words)
# i=0
# x=[]
# while i<len(words):
#     a=len(words[i])
#     x.append(a)
#     i+=1
#     long=max(x)
#     longest=words[long]
# print("longest word is:",longest)
# # print(x)


# file=open("longest_word.txt")
# file1=file.read()
# word=file1.split()
# print(word)
# max=word[0]
# i=0
# while i<len(word):
#   if len(word[i])>len(max):
#     max=word[i]
#   i+=1
# print("The longest word is:",max)


file=open(input("enter file name:"))
file1=file.read()
word=file1.split()
# print(word)
max=word[0]
i=0
while i<len(word):
  if len(word[i])>len(max):
    max=word[i]
  i+=1
print("The longest word is:",max)