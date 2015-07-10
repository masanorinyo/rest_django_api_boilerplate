# This file makes sure that "sniffer" module catches any changes added to the code and re-run the test scripts based on the changes.

from subprocess import call
from sniffer.api import runnable

@runnable
def execute_tests(*args):
    fn = [ 'python', 'manage.py', 'test' ]
    fn += args[1:]
    return call(fn) == 0