import csv
import os
import pandas as pd

import re
import converter as conv
import cleaner as clr
import usersentencedivert as usd
import twitterhandler as twk
def paragraghdiversion(s1):
    import re
    import csv
    list1=[]
    s =s1 
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', s)
    for i in m:
        list1.append(i)
        #print(list1)
        j=len(list1)
        #print (j)
        list2=[]
    for i in range(j):
        list2.append(i)
               
    filename = "sample.csv"
    fields = ['id', 'review'] 
# writing to csv file 
    with open(filename, 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        writer.writeheader() 
        for i in range(j):
            mydict =[{'id':i, 'review': list1[i]}]
            writer.writerows(mydict)