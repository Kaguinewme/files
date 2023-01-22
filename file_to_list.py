file=open("file_to_list.txt")
print(file.readlines())
file.close()

def list(file_name):
    file=open(file_name)
    print(file.readlines())
list("file_to_list.txt")

# file=open("file_to_list.txt")
# file1=file.read()
# words=file1.split()
# print(words)