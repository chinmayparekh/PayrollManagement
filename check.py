
# Displaying Employee File   
def display_emp():
    fin = open('employee_file.txt','r')
    print('\n')
    print(70 * "*", " EMPLOYEE PAY FILE ", 69 * "*")
    print(160 * '-')
    print('ENO  NAME\tGENDER DOB\t  DOJ\t     DESIGNATION\t\t      BASIC($)  PHONE       MOBILE      ADDRESS')
    print(160 * '-')
    for line in fin:
        line = line.strip()
        data = line.split(',')
        eno, na, gen, dob, doj, desig, bs, pnum, mnum, add = int(data[0]), data[1], data[2], data[3], data[4], data[5], float(data[6]), int(data[7]), int(data[8]), data[9]
        print('%i %-10s %s      %4s %s %-32s %-7.0f   %i  %i  %s'%(eno, na, gen, dob, doj, desig, bs, pnum, mnum, add))
    print(160 * '-')
    print('\nEMPLOYEE FILE DISPLAYED SUCCESSFULLY!')
    fin.close()
    print('\n')

# Displaying Monthly Pay File
def display_mon():
    x = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    a = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    print('\n')
    print('*' * 23,'\tMONTHLY PAY FILE (' +  x[m - 1] + '-', str(y) + ')\t', '*' * 22)
    print(87 * '-')
    print('ENO\t NAME\tDESIGNATION\t\t\tBASIC\t GROSS\t DEDUCTIONS\t NET')
    print(87 * '-')
    file_name = 'Monthly_pay' + '_' + x[m - 1] + '_' + str(y) + '.txt' 
    try: 
        fin = open(file_name, 'r')
        for line in fin:
            line = line.strip()
            arr = line.split(',')
            ded = int(arr[9]) + int(arr[10])
            print(arr[0], '\t', arr[1], '\t', arr[2], '\t', arr[4], '\t', arr[8], '\t', ded, '\t\t', arr[11])
        print(87 * '-')
        print('\nMONTHLY PAY FILE FOR',a[m - 1],str(y),'DISPLAYED SUCCESSFULLY!\n') 
    except:
        print("\nERROR: MONTHLY PAY FILE FOR",a[m - 1],str(y),"DOESN'T EXIST!\n")