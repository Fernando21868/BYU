from tasks import Task, format_data, validation
import pytest


def test_format_data():
    assert format_data('homework') == 'HOMEWORK'
    assert format_data('CoOkInG') == 'COOKING'
    assert format_data('Fishing') == 'FISHING'
    assert format_data('EATing') == 'EATING'
    assert format_data('    work    ') == 'WORK'
    assert format_data('        cLEAN Up   ') == 'CLEAN UP'
    assert format_data('  drive ') == 'DRIVE'


def test_validation():
    assert validation('Homework', 'I have to do homework') == True
    assert validation('', '') == False
    assert validation('', 'I have to fish to get the food') == False
    assert validation('Eating', '') == False
    assert validation('Work', 'I have to going to the work') == True
    assert validation(
        '     Clean up', '    I have to clean up the house') == True
    assert validation('  Drive  ', 'I have to do homework') == True
    assert validation('    ', '   ') == False


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
