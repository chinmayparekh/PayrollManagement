import pytest
from payment import modif1,display_emp,modif2,modif3,modif4,dateval,
import os
def test_modif1_yes(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['Engineer', '5000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif1('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,10000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY UPDATED SUCCESSFULLY!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif1_no(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['Engineer', '5000', 'N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif1('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY NOT UPDATED!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif1_not_found(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['Nonexistent', '5000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif1('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: DESIGNATION NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif1_empty_file(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['Engineer', '5000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an empty file
    open('test_empty_file.txt', 'w').close()

    # Call the function with the empty file
    modif1('test_empty_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: DESIGNATION NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_empty_file.txt')
    os.remove('test_temporary.txt')

def test_modif2_yes(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'Manager', '6000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif2('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,MANAGER,6000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'DESIGNATION UPDATED SUCCESSFULLY!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif2_no(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'Manager', '6000', 'N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif2('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif2_invalid_input(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', '123', 'Manager', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif2('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Please enter proper Designation and Basic Salary' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif2_employee_not_found(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['2', 'Manager', '6000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif2('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif2_empty_file(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'Manager', '6000', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an empty file
    open('test_empty_file.txt', 'w').close()

    # Call the function with the empty file
    modif2('test_empty_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_empty_file.txt')
    os.remove('test_temporary.txt')

def test_modif3_yes(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'F', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif3('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,F,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change?\n\tY/y for Yes or N/n for No' in out
    assert 'GENDER UPDATED!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif3_no(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'F', 'N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif3('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change?\n\tY/y for Yes or N/n for No' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif3_not_found(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['2', 'F', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif3('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif3_invalid_gender(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'X'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif3('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Please enter Gender as either F- Female or M- Male' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif3_empty_file(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', 'F', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an empty file
    open('test_empty_file.txt', 'w').close()

    # Call the function with the empty file
    modif3('test_empty_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_empty_file.txt')

def test_modif4_yes(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', '15', '05', '1995', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif4('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,15-05-1995,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change?\n\tY/y for Yes or N/n for No' in out
    assert 'DATE OF BIRTH UPDATED SUCCESSFULLY!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif4_no(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', '15', '05', '1995', 'N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif4('test_employee_file.txt', 'test_temporary.txt')

    # Check the contents of the temporary file
    with open('test_employee_file.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change?\n\tY/y for Yes or N/n for No' in out
    assert 'DATE OF BIRTH NOT UPDATED!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif4_not_found(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['2', '15', '05', '1995', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a temporary file with test data
    with open('test_employee_file.txt', 'w') as f:
        f.write('1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n')

    # Call the function with the test file
    modif4('test_employee_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')

def test_modif4_empty_file(monkeypatch, capfd):
    # Mock the input function
    inputs = iter(['1', '15', '05', '1995', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an empty file
    open('test_empty_file.txt', 'w').close()

    # Call the function with the empty file
    modif4('test_empty_file.txt', 'test_temporary.txt')

    # Check the print statements
    out, err = capfd.readouterr()
    assert '\nERROR: EMPLOYEE NUMBER NOT FOUND!\n' in out

    # Clean up the test files
    os.remove('test_empty_file.txt')


def test_dateval():
    # Test valid dates
    assert dateval(15, 5, 1995) == '15-05-1995'
    assert dateval(1, 1, 1950) == '01-01-1950'
    assert dateval(31, 12, 2001) == '31-12-2001'

    # Test invalid day
    with pytest.raises(Exception, match='Please input valid Day'):
        dateval(32, 5, 1995)

    # Test invalid month
    with pytest.raises(Exception, match='Please input valid Month'):
        dateval(15, 13, 1995)

    # Test leap year
    assert dateval(29, 2, 2000) == '29-02-2000'

    # Test non-leap year
    with pytest.raises(Exception, match='Please input valid Day'):
        dateval(29, 2, 2001)

    # Test year out of range
    with pytest.raises(Exception, match='Please input valid Year between 1950 and 2001'):
        dateval(15, 5, 1949)

    with pytest.raises(Exception, match='Please input valid Year between 1950 and 2001'):
        dateval(15, 5, 2002)

    # Test month with 30 days
    assert dateval(30, 4, 2000) == '30-04-2000'
    with pytest.raises(Exception, match='Please input valid Day'):
        dateval(31, 4, 2000)

    # Test month with 31 days
    assert dateval(31, 5, 2000) == '31-05-2000'

import re

def test_display_emp_valid_file(capfd):
    # Assuming valid_employee_file.txt exists and contains valid data
    display_emp('employee_file.txt')
    out, err = capfd.readouterr()
    assert 'ENO  NAME\tGENDER DOB\t  DOJ\t     DESIGNATION\t\t      BASIC($)  PHONE       MOBILE      ADDRESS' in out

def test_display_emp_empty_file(capfd):
    # Create an empty file
    display_emp('empty.txt')
    out, err = capfd.readouterr()
    assert '\nEMPLOYEE FILE DISPLAYED SUCCESSFULLY!' in out