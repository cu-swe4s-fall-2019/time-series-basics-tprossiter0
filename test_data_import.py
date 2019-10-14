import unittest
import random
import sys
import os.path
import data_import as datimp
from os import path


class TestDataImport(unittest.TestCase):
    def testImportDataEmptyValues(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        file.write("testtime, testvals \n")
        for n in range(0: 100):
            file.write("test" + str(n) + " " + 1 + "\n")
        for n in range(0: 10):
            file.write("test" + str(n+100) + "   \n")
        testobject = data_import(test_filename)
        self.assertEqual(100, len(testobject._value))
