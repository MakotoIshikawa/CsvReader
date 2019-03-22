from commonlib import BatchFileFactory

if __name__ == '__main__':
    of = BatchFileFactory('..\\data\\jp1_TDB01.csv')
    of.create()
