import csv
import sys
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime
import math


class ImportData:
    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._rdtime = []
        self._data = data_csv
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
        """
        Search the time list for key_time, return corresponding values to that time
        Parameters
        --------------
        self (the object, selfcall)
        key_time <- time to search for corresponding values

        Returns
        --------------
        values_to_return <- list of values parallel to the key_time, if they exist
        """
        if(key_time is None):
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

def roundTimeArray(obj, res):
    """ Return zipped list of rounded times and their corresponding values(operated on)

    Parameters
    ----------
    obj, an instance of the ImportData class

    Returns
    ----------
    a list of two lists zipped together:
        newvaluearr <- list of sums or averages of all the times, parallel to the rounded times
        newtimearr <- list of rounded times 

    """
    sums = ["activity_small.csv", "meal_small.csv", "bolus_small.csv"]
    avgs = ["Smbg_small.csv", "Hr_small.csv", "Cgm_small.csv", "Basal_small.csv"]

    newminutes = []
    try:
        intervals = 60/res + 1
    except ValueError:
        print("res must be integer")

    tempvalues = []
    newtimearr = []
    newvalarr = []
    i_loop = 0
    for time in obj._time:
        # compute rounded time
        rdtime = time
        tempminutes = time.minute + time.second/60
        minutedifference = tempminutes % res
        if(minutedifference > (res/2)):
            tempminutes = tempminutes - minutedifference + res
        else:
            tempminutes = tempminutes - minutedifference


        if(tempminutes == 0 and rdtime > 30):
            rdtime = rdtime.replace(hour=rdtime.hour + 1, minute = int(tempminutes))
        else:
            rdtime = rdtime.replace(minute=int(tempminutes))

        #store new time in newtimearr
        #store local group of times in temptimes
        index_of_time = -1
        for j in range(0, len(newtimearr)):
            if rdtime == newtimearr[j]:
                index_of_time = j

        if(index_of_time == -1 and i_loop == 0):
            newtimearr.append(rdtime)
            tempvalues.append(obj._value[i_loop])

        if(index_of_time != -1):
            tempvalues.append(obj._value[i_loop])

        if(index_of_time == -1 and i_loop > 0):
            for k_loop in range(0,len(sums)):
                if(obj._data == sums[k_loop]):
                    print("summing")
                    newvalarr.append(sum(tempvalues))

            for k_loop in range(0,len(avgs)):
                if(obj._data == avgs[k_loop]):
                    newvalarr.append(avg(tempvalues))

            tempvalues = [obj._value[i_loop]]
        
        if(i_loop == len(obj._time)):
            for k_loop in range(0,len(sums)):
                if(obj._data == sums[k_loop]):
                    print("summings")
                    newvalarr.append(sum(tempvalues))

            for k_loop in range(0,len(avgs)):
                if(obj._data == avgs[k_loop]):
                    newvalarr.append(avg(tempvalues))

        i_loop = i_loop + 1

    rlist = list(zip(newtimearr, newvalarr))
    return rlist
        #when new rdtime is hit, compute avg or sum -> newvalarr




        


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
    files_lst = # list the folders


    #import all the files into a list of ImportData objects (in a loop!)
    data_lst = []
    for n in files_list:
        data_lst.append(ImportData(n))

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
