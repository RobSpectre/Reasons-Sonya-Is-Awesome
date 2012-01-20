import unittest
import web_test

def runTests(verbosity=2):
    # Loader
    loader = unittest.TestLoader()

    # Suite
    suite = unittest.TestSuite()

    # Load test suite
    suite.addTests(loader.loadTestsFromModule(web_test))
    
    # Run test suite
    runner = unittest.TextTestRunner(verbosity=verbosity)
    return runner.run(suite)

if __name__ == "__main__":
    runTests()
