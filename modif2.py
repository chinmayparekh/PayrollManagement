def modif2(file_name):
    fin = open(file_name, 'r')
    fout = open('temporary.txt', 'w')
    no = input('Employee Number to change Designation? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == int(no):
            found = 1
            print('Name :', arr[1])
            print('Designation:', arr[5], '\t\t', 'Basic Salary :', arr[6])
            newdes = input('New Designation? ')
            newbs = input('New Basic Salary? ')
            while not newdes.isalpha() or not newbs.isdigit():
                print('Please enter proper Designation and Basic Salary')
                newdes = input('New Designation? ')
                newbs = input('New Basic Salary? ')
            print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdes.upper()
                arr[6] = newbs
                print('DESIGNATION UPDATED SUCCESSFULLY!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    if found == 1:
        remove(file_name)
        rename('temporary.txt', file_name)
    