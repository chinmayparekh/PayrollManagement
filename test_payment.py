import pytest
from payment import modif1

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