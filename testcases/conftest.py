import logging
import pytest
from _pytest.runner import runtestprotocol
from _pytest.main import EXIT_OK, EXIT_TESTSFAILED, EXIT_INTERRUPTED, \
    EXIT_USAGEERROR, EXIT_NOTESTSCOLLECTED

@pytest.hookimpl(trylast=True)
def pytest_sessionstart(session):
    print("********************* start *********************")


def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            print('%s --- %s' % (item.name, report.outcome))
    
    return True

def pytest_sessionfinish(exitstatus):
    print("********************* finish *********************")
    if exitstatus == EXIT_OK:
        print('TEST PASS!!!')
    
    if exitstatus == EXIT_TESTSFAILED:
        print('TEST FAILED!!!')


