import unittest
from commonlib import BatchFileFactory

class Test_test1(unittest.TestCase):
    def test_output_batch_file(self):
        of = BatchFileFactory('..\\data\\jp1_TDB01.csv')
        of.create()
        of.file_name = '..\\data\\jp1_TDB02.csv'
        of.create()
        of.file_name = '..\\data\\jp1_TDB03.csv'
        of.create()

if __name__ == '__main__':
    unittest.main()
