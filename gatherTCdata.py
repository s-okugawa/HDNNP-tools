import os
import csv
from itertools import islice

root=os.getcwd()
node=["50", "100", "200", "300", "500"]

with open('TCdata.csv', 'w') as TC:
    writer = csv.writer(TC, lineterminator='\n')
    for k in range(20, 110, 20):
        for i in node:
             for j in range(1, 11):
                infile =root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phono3py/out.txt"
                with open(infile, 'r') as infl:
                    for n, line in enumerate(infl):
                         if 'Thermal conductivity (W/m-k)' in line:
                            infl.seek(0)
                            TCdt=[]
                            for lined in islice(infl, n+12, n+112, 10):
                                data=lined.split()
                                TCdt.append(float(data[1]))
                            writer.writerow(TCdt)
