# -*- coding: utf-8 -*-

import glob
import csv
import sys

csv.field_size_limit(sys.maxsize)


path = r'your cvs path'

business_no = [] # to delete overlapping value, check business number
def check(string) :
    global business_no
    business_no.insert(0, string)

for csvf in glob.glob(pathname=path + '\*.csv') :
    count = 0
    f = open(csvf,'r',encoding="UTF-8",errors='ignore')
    reader = csv.reader(f)
    for line in reader :
        count += 1
        nm = 0
        for k in line :
            if nm == 3 and count >= 4 : # check a specific cell
                if k is not '' :
                    check(str(k))
                    break
            else :
                nm += 1
    f.close()
    
business_no = list(set(business_no))
print(len(business_no)) # print the number of businesses
