# -*- coding: utf-8 -*-
import os
import csv
import ast

if __name__ == '__main__': 
    root=os.getcwd()
    outfile= root+"/RMSEdata.csv"
    node=["50", "100", "200", "300", "500"]

    with open(outfile, 'w') as f1:
        writer = csv.writer(f1, lineterminator='\n')

        for k in range(20, 110, 20):
            for i in node:
                 for j in range(1, 11):
                    logfile= root+"/d"+str(k)+"n"+i+"/"+str(j)+"/output/CrystalSi64/training.log"
                    with open(logfile, 'r') as infl:
                        logdata= infl.read()
                        listdata= ast.literal_eval(logdata)
                        lastdata=listdata[-1]
                        outdata=[]
                        outdata.append(int(lastdata["epoch"]))
                        outdata.append(float(lastdata["val/main/RMSE/force"]))
                        writer.writerow(outdata)
