import unittest
from time import time
from blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain()

    def test_chain(self):
        self.assertIsInstance(self.bc.chain, list)

    def test_current_transactions(self):
        self.assertIsInstance(self.bc.current_transactions, list)

    def test_new_block(self):
        self.assertIsInstance(self.bc.new_block(proof=200), dict)
        self.assertEqual(len(self.bc.chain), 2)

    def test_hash(self):
        block = {
            'index': 1,
            'timestamp': time(),
            'transactions': [],
            'proof': 123,
            'previous_hash': None
        }

        self.assertIsInstance(Blockchain.hash(block), str)

    def test_last_block(self):
        self.bc.new_block(123)
        self.assertIsInstance(self.bc.last_block, dict)

    def test_new_transaction(self):
        new_transaction_return = self.bc.new_transaction('alex', 'daniel', 1000)
        expected = self.bc.last_block['index'] + 1
        self.assertEqual(new_transaction_return, expected)
        self.assertEqual(len(self.bc.current_transactions), 1)

    def test_proof_of_work(self):
        self.assertIsInstance(self.bc.proof_of_work(1), int)


def test_suite():
    new_suite = unittest.TestSuite()
    new_suite.addTest(unittest.makeSuite(TestBlockchain))
    return new_suite

BlockChainTestSuite = test_suite()

runner = unittest.TextTestRunner()
runner.run(BlockChainTestSuite)
if __name__ == '__main__':
    unittest.main()
