# file=open("last_n_lines.txt")
# num=int(input("enter number:"))
# f=file.readline()
# while num>0:
#     print(f[-num:])
#     num-=1



file=open("last_n_lines.txt")
f=file.readlines()
line=int(input("Enter a line to be read from last:"))
print(f[-line:])


# file=open("first_n_lines.txt")
# num=int(input("enter number:"))
# while num>0:
#     f=file.readline()
#     print(f[-num:])
#     num+=1