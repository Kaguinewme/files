def count(file_name):
    file=open(file_name)
    f=file.readlines()
    print(len(f))
count("count_lines.txt")