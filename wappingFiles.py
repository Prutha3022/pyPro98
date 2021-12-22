def countWordsFromFile():
    file1 =  input("Enter the file name1:- ")
    file2 =  input("Enter the file name2:- ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as a:
        data_b = a.read() 

    with open(file1, 'w') as a:
        a.write(data_b) 

    with open(file2, 'w') as a:
        a.write(data_a)       

countWordsFromFile()