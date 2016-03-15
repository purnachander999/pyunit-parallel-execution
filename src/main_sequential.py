'''
Created on Mar 15, 2016

@author: purna chander
'''

import unittest, sys

import testcases.regression_test_1
import testcases.regression_test_2


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.BaseTestSuite()
    
 


    suite.addTests(loader.loadTestsFromModule(testcases.regression_test_1))
    suite.addTests(loader.loadTestsFromModule(testcases.regression_test_2))
    
    #runner = unittest.TextTestRunner() 
    
    isSuccessful = True
    testsRan = False
    
    #isSuccessful = runner.run(suite)
    isSuccessful = unittest.TextTestRunner(verbosity = 2).run(suite).wasSuccessful()

    if isSuccessful:
        sys.exit(0)

    sys.exit(1)
    