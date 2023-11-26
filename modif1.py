# Modification in Basic Salary
def modif1(file_name):
    fin = open(file_name, 'r')
    fout = open('temporary.txt', 'w')
    desig = input('Designation to change Basic Salary? ')
    inc = int(input('Amount by which Basic Salary to be increased? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if arr[5] == desig.upper():
            found = 1
            print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n] ')
            if ch == 'Y' or ch == 'y':
                arr[6] = str(int(arr[6]) + inc)
                print('BASIC SALARY UPDATED SUCCESSFULLY!\n')
            else:
                print('BASIC SALARY NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: DESIGNATION NOT FOUND!\n')
    fin.close()
    fout.close()
    if found == 1:
        remove('employee_file.txt')
        rename('temporary.txt', 'employee_file.txt')
