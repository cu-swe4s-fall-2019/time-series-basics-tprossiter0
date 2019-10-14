import unittest
import random
import sys
import os.path
import datetime
import dateutil.parser
from data_import import ImportData as idata
from os import path


class TestDataImport(unittest.TestCase):
    def testImportDataEmptyValues(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")
        for n in range(0, 100):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + "," + str(1) + "\n")

        for n in range(0, 10):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + "," + "\n")

        test_file.close()
        testobject = idata(test_filename)
        self.assertEqual(100, len(testobject._value))
        test_filename


if __name__ == '__main__':
    unittest.main()
