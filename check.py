def modif2(file_name,ttfile,n,dg,sal,cnf):
        fin = open(file_name, 'r')
        fout = open(ttfile, 'w')
        no = n
        found = 0
        for data in fin:
            data = data.strip()
            arr = data.split(',')
            if int(arr[0]) == int(no):
                found = 1
                print('Name :', arr[1])
                print('Designation:', arr[5], '\t\t', 'Basic Salary :', arr[6])
                newdes = dg
                newbs = sal
                while not newdes.isalpha() or not newbs.isdigit():
                    print('Please enter proper Designation and Basic Salary')
                    exit(0)
                print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
                ch = cnf
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
