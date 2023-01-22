# file=open("seperate_list.txt")
# a=file.readlines()
# print(a)
# i=0
# while i<len(a):
#     if "delhi" in a[i]:
#         x=open("delhi.txt","w")
#         x.write(a[i])
#     elif "shimla" in a[i]:
#         y=open("shimla.txt","w")
#         y.write(a[i])
#     else:
#         z=open("others.txt","w")
#         z.write(a[i])
#     i+=1
# file.close()



f=open("separate_list.txt","r")
a=f.readlines()
x=open("delhi.txt","w")
y=open("shimla.txt","w")
z=open("others.txt","w")
i=0
while i<len(a):
    if "delhi" in a[i]:
        x.write(a[i])
    elif "shimla" in a[i]:
        y.write(a[i])
    else:
        z.write(a[i])
    i+=1
f.close()
# x.close()
# y.close()
# z.close()