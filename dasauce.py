from os import listdir
import csv
import sys
import os
import os.path
import datetime

total = []

def write_txt(file):
    with open(file, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			total.extend(row)

mypath = raw_input('Please enter directory of CSV files: ')
mypath = str(mypath)
mypath.replace(r"/DIR/", mypath)
# mypath = 'C:\\Users\\Justin\\Desktop\\DaSauce\\test_folder' Example if you want to hardcode it

files = os.listdir(mypath)

for file in files:
	if file.endswith(".csv"):
		full = mypath + '\\' + file
		write_txt(full)	
		
print total

for x in range(int(min(total, key=int)), int(max(total, key=int)) + 1):
	print ("{0} occurred {1} times which is {2}% of total".format(x, total.count(str(x)), (float(total.count(str(x))) / ( float(len(total)))) * 100 ))
	
save = raw_input('Would you like to save this information? (Y/N): ')

if (str(save).lower() == 'y'):
	now = datetime.datetime.now()
	new_path = mypath + "\\output_" + str(now.day) + "_" + str(now.month) + "_" + str(now.year) + ".txt"
	file = open(new_path, 'w+')
	for y in range(int(min(total, key=int)), int(max(total, key=int)) + 1):
		file.write("{0} occurred {1} times which is {2}% of total\n".format(y, total.count(str(y)), (float(total.count(str(y))) / ( float(len(total)))) * 100 ))
	file.close()
	print "File successfully saved to " + new_path
