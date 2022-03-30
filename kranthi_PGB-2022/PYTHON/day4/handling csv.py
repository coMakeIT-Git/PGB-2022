
# Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names
import csv
def csv_file():
    csvfile = input("Enter CSV File Name (csvfile.csv) : ")
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Total Number of Rows : {sum(1 for line in reader)}")
        print(f"Total Number of columns : {len(headers)}")
        print(f"feild Names : {headers}")


csv_file()