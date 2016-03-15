'''
Created on Mar 15, 2016

@author: purna chander
'''

import unittest, sys

import testcases.regression_test_1
import testcases.regression_test_2

from concurrencytest import ConcurrentTestSuite, fork_for_tests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.BaseTestSuite()

    suite.addTests(loader.loadTestsFromModule(testcases.regression_test_1))
    suite.addTests(loader.loadTestsFromModule(testcases.regression_test_2)) 
       

    runner = unittest.TextTestRunner()

    isSuccessful = True
    testsRan = False
    

    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(10))
    isSuccessful = runner.run(concurrent_suite)
    
    if isSuccessful:
        sys.exit(0)

    sys.exit(1)
    