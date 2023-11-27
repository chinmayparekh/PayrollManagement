import pytest
from payment import modif1,display_emp
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
    with open('test_temporary.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,10000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY UPDATED SUCCESSFULLY!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')
    os.remove('test_temporary.txt')

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
    with open('test_temporary.txt', 'r') as f:
        data = f.read()
    assert '1,John,M,1990,2020,ENGINEER,5000,1234567890,9876543210,123 Street\n' in data

    # Check the print statements
    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY NOT UPDATED!\n' in out

    # Clean up the test files
    os.remove('test_employee_file.txt')
    os.remove('test_temporary.txt')

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
    os.remove('test_temporary.txt')

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