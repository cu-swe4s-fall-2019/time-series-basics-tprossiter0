import csv
import sys
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime


class ImportData:
    def __init__(self, data_csv):
        self._time = []
        self._value = []

        with open(data_csv) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["time"] is "" or row["value"] is "":
                    continue
                    print("empty values here")
                else:
                    try:
                        self._time.append(dateutil.parser.parse(row["time"]))
                    except ValueError:
                        print("can't parse time properly")
                        print(row["time"])
                        sys.exit(1)

                    if(row["value"] == "high"):
                        try:
                            self._value.append(300)
                            print("'high' value entered as 300")
                        except ValueError:
                            print("can't append " + row["value"])

                    elif(row["value"] == "low"):
                        try:
                            self._value.append(40)
                            print("'low' value entered as 40")
                        except ValueError:
                            print("can't append " + row["value"])
                    if(row["value"] != "high" and row["value"] != "low"):
                        newval = int(row["value"])
                        try:
                            self._value.append(newval)
                        except ValueError:
                            print("can't parse values properly")
                            print(row["value"])
                            sys.exit(1)
            csvfile.close()
        # open file, create a reader from csv.DictReader, and read input times and values

    def linear_search_value(self, key_time):
        if(key_time is None);
            print("key_time argument is required to use this method")
            return -1
        if(isinstance(key_time, datetime.datetime) is False):
            raise Exception("key_time requires type datetime")
            sys.exit(1)

        values_to_return = []
        if(isinstance(key_time, datetime.datetime)):
            for n in range(0, len(self._time)):
                if(key_time == self._time[n]):
                    values_to_return.append(self._value[n])
        return values_to_return







        # return list of value(s) associated with key_time
        # if none, return -1 and error message

    #def binary_search_value(self,key_time):

        # optional extra credit
        # return list of value(s) associated with key_time
        # if none, return -1 and error message

#def roundTimeArray(obj, res):
    
    # Inputs: obj (ImportData Object) and res (rounding resoultion)
    # objective:
    # create a list of datetime entries and associated values
    # with the times rounded to the nearest rounding resolution (res)
    # ensure no duplicated times
    # handle duplicated values for a single timestamp based on instructions in
    # the assignment
    # return: iterable zip object of the two lists
    # note: you can create additional variables to help with this task
    # which are not returned


#def printArray(data_list, annotation_list, base_name, key_file):
    
    # combine and print on the key_file

if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type=str, help='Name of the folder')

    parser.add_argument('output_file', type=str, help='Name of Output file')

    parser.add_argument('sort_key', type=str, help='File to sort on')

    parser.add_argument('--number_of_files', type=int,
    help = "Number of Files", required=False)

    args = parser.parse_args()


    #pull all the folders in the file
    ##files_lst = # list the folders


    #import all the files into a list of ImportData objects (in a loop!)
    ##data_lst = []

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
