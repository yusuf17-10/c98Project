def swapFileData():
    file1=input("enter the file that you want to swamp")
    with open(file1, "r") as a:
        data__a = a.read()
    with open(file2, "r") as b:
        data__b = b.read()
    
    with open(file1, "w") as a:
        a.write(data_b)

    with open(file2, "w") as b:
        b.write(data_a)

swapFileData()