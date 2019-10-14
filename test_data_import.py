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
    
    def testImportDataHighLow(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")
        testarray = []
        for n in range(0,20):
            if(n < 10):
                testarray.append(300)
            if(n > 10):
                testarray.append(40)

        for n in range(0, 100):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + "," + str(1) + "\n")

        for n in range(0, 10):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + ",high" + "\n")

        for n in range(0, 10):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + ",low" + "\n")
        test_file.close()
        testobject = idata(test_filename)

        self.assertEqual(testarray, testobject._value[100 : 120])
        
if __name__ == '__main__':
    unittest.main()
