# -*- coding: utf-8 -*-
import os
import csv
import ast
from itertools import islice

"""
This script is made to output csv file by gathering 
1) force/RMSE & difference of train/validation & TC(300K) diff from 112.1 
2) train curve data (epoch, trained force/RMSE, validated, difference))
from all RMSE data and TC data
"""

if __name__ == '__main__': 
    root=os.getcwd()

    tdata=["5","20","40","60","80","100"]
    node=["50","100","200","300","500"]
    rstfile=root+"/result/RMSEdata.csv"
    traindir=root+"/result/traincv/"
    
    with open(rstfile, 'w') as rslt:
        writer1 = csv.writer(rslt, lineterminator='\n')
        for k in tdata:
            for i in node:
                for j in range(1, 11):
                    logfile= root+"/d"+k+"n"+i+"/"+str(j)+"/output/CrystalSi64/training.log"
                    traincvfile= traindir+"d"+k+"n"+i+"-"+str(j)+".csv"

                    with open(logfile, 'r') as log:
                        logdata= log.read()
                        listdata= ast.literal_eval(logdata)
                        listlen= len(listdata)
                        diffnum=0
                        difftotal=0
                        with open(traincvfile, 'w') as tcv:
                            writer2 = csv.writer(tcv, lineterminator='\n')
                            for epc in range(9, listlen, 10):
                                ep=int(listdata[epc]["epoch"])
                                tf=float(listdata[epc]["main/RMSE/force"])*1000
                                vf=float(listdata[epc]["val/main/RMSE/force"])*1000
                                diff=vf-tf
                                outdata=[ep]+[tf]+[vf]+[diff]
                                writer2.writerow(outdata)
                                if epc > listlen-200:
                                    diffnum=diffnum+1
                                    difftotal=difftotal+diff
                            diffave=difftotal/diffnum
                    
                    infile =root+"/d"+k+"n"+i+"/"+str(j)+"/predict-phono3py/out.txt"
                    with open(infile, 'r') as infl:
                        for n, line in enumerate(infl):
                            if 'Thermal conductivity (W/m-k)' in line:
                                infl.seek(0)
                                for lined in islice(infl, n+32, n+33):
                                     data=lined.split()
                                     TCerr=abs(float(data[1])-112.1)

                    RMSEdt=[vf]+[diffave]+[TCerr]
                    writer1.writerow(RMSEdt)

