import pytest
from payment import modif1,display_emp
import re
def test_modif1_yes(capfd):
    modif1('employee_file.txt', 'temporary.txt', 'Manager', 1000, 'Y')

    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY UPDATED SUCCESSFULLY!\n' in out

def test_modif1_no(capfd):
    modif1('employee_file.txt', 'temporary.txt', 'Manager', 1000, 'N')

    out, err = capfd.readouterr()
    assert 'Are you sure you want to change:\n\tY/y for Yes or N/n for No' in out
    assert 'BASIC SALARY NOT UPDATED!\n' in out

def test_modif1_not_found(capfd):
    modif1('employee_file.txt', 'temporary.txt', 'Nonexistent', 1000, 'Y')
    out, err = capfd.readouterr()
    assert '\nERROR: DESIGNATION NOT FOUND!\n' in out

def test_modif1_empty_file(capfd):
    modif1('empty.txt', 'temporary.txt', 'Nonexistent', 1000, 'Y')
    out, err = capfd.readouterr()
    assert '\nERROR: DESIGNATION NOT FOUND!\n' in out

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