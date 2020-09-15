"""
Lecture covers working aith CS files in python
"""
import csv

# A CSV file only contains raw data from a spread sheet
# Other python libraries to consider when working with CSV'c Pandas,
# Openpyxl, Google Sheets Python API


#exercise
# open file
data = open('example.csv', encoding='utf-8')

#read file
csv_data = csv.reader(data)

#turn in to pyrhon object
#data_lines = list(csv_data) will result in error if encoding is not included
data_lines = list(csv_data)
print(data_lines)
