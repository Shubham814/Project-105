import csv
with open('data_105.csv',newline='') as f:
  data = csv.reader(f)
  fileData = list(data)

file_data = fileData[0]
arrayLen = len(file_data)

addition = 0
for i in file_data:
  addition = addition + int(i)
mean = int(addition) / int(arrayLen)

array = []
for i in file_data:
  thirdStep = int(i) - mean
  fourthStep = thirdStep**2
  array.append(fourthStep)

total = 0
for i in array:
  total = total + int(i)

import math
standard_deviation = math.sqrt(total/arrayLen)
print("\nStandard Deviation is " + str(standard_deviation))