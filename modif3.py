
# Modification in Gender
def modif3():
    fin = open('employee_file.txt', 'r')
    fout = open('temporary.txt', 'w')
    no = input('Employee Number to change Gender? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == int(no):
            found = 1
            print('Name :', arr[1])
            print('Gender:', arr[2])
            gender = input('Gender [F/M]? ')
            while gender.upper() != 'F' and gender.upper() != 'M':
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[2] = gender.upper()
                print('GENDER UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    if found == 1:
        remove('employee_file.txt')
        rename('temporary.txt', 'employee_file.txt')
