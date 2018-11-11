import unittest
from blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    pass


def test_suite():
    new_suite = unittest.TestSuite()
    new_suite.addTest(unittest.makeSuite(TestBlockchain))
    return new_suite

BlockChainTestSuite = test_suite()

runner = unittest.TextTestRunner()
runner.run(TestBlockchain)
# if __name__ == '__main__':
#   unittest.main()
