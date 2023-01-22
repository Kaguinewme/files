file=open("append_read.txt","a")
file.write("\n"+"text file and binary file.")
file.close()
file=open("append_read.txt")
print(file.read())
file.close()


# def append_file(file_name):
#     file=open(file_name,"a")
#     file.write("\n"+"append to the end of a file.")
#     file.close()
#     file=open(file_name)
#     print(file.read())
# append_file("append_read.txt")