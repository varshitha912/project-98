def swapefiledata():
    file1=input("Enter the file name- ")
    file2=input("Destination file name- ")
    with open(file1,'r')as a:
        data_A=a.read()
    with open(file2,'r')as b:
        data_B=b.read()
    with open(file1,'w')as a:
        a.write(data_B)
    with open(file2,'w')as b:
        b.write(data_A)
swapefiledata()