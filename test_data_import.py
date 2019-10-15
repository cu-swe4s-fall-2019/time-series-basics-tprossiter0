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

    def testImportDataHighLow(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")
        testarray = []
        for n in range(0, 100):
            testarray.append(1)
        for n in range(0, 20):
            if(n < 10):
                testarray.append(300)
            if(n >= 10):
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

        self.assertEqual(testarray, testobject._value[0: 120])

    def testImportDataIntegers(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")
        testarray = []
        for n in range(0, 100):
            testarray.append(1)
        for n in range(0, 20):
            if(n < 10):
                testarray.append(300)
            if(n >= 10):
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
        testallints = 0

        for n in testobject._value:
            if isinstance(n, int):
                testallints = testallints + 1

        self.assertEqual(120, testallints)

    def testTimeDateTime(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")

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
        testalldatetimes = 0
        for n in testobject._time:
            if isinstance(n, datetime.datetime):
                testalldatetimes = testalldatetimes + 1
        self.assertEqual(120, testalldatetimes)

    def testLinearSearchWrongInput(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.write("time,value\n")
        for n in range(0, 100):
            tempdate = str(datetime.datetime.now())
            test_file.write(tempdate + "," + str(1) + "\n")
        test_file.close()
        testobject = idata(test_filename)
        testobject.linear_search_value(datetime.datetime.now())
        with self.assertRaises(Exception) as ex:
            testobject.linear_search_value(76)
        output = str(ex.exception)
        self.assertEqual(output, "key_time requires type datetime")


if __name__ == '__main__':
    unittest.main()
