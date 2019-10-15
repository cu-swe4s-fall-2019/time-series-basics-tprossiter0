# time-series-basics
Time Series basics - importing, cleaning, printing to csv

## Usage

- Data_Import.py
Contains Class ImportData
--Initialization requires name of a csv with headers 'time', and 'value'
--Contains method to linearly search the values corresponding to a given "time" argument

Contains function roundTimeArray()
--Takes an object of type ImportData and a time resolution (integer)

This function returns a "zipped" list of time values rounded to the nearest resolution, and their corresponding values
 	Values that correspond to the same rounded time will be summed or averaged depending on the file read into the ImportData object
*Functionality currently unavailable*
Further unit-testing required for this function.
Lack of building many, modular unit tests contributed to lack of functionality learned the hard way!


## Testing
Testing only operating in test_data_import.py
- includes tests for correct arguments given to the initialization of ImportData
- includes functionality tests for Import Data init, 
	Makes sure, high, low values are converted to 400, 30
	Makes sure only integer values are present in the value list

## Minimum Requirements to operate with files

- Python 3.7.4
- All modules included in Python default libraries, like datetime, sys, argparse etc

Note date files are synthetic data. 
