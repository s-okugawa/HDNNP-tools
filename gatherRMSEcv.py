# -*- coding: utf-8 -*-
import os
import sys
import csv
import ast
"""
This script is made to output csv file of selected force/RMSE data 
Usage:
$ python gatherRMSEcv.py [out dir] [dxxnyy/zz] [dxxnyy/zz] ...
out dir: output directory
dxxnyy/zz : data directory - xx=trained data#, yy=node#, zz=repeat#
"""

if __name__ == '__main__': 
    root=os.getcwd()

    args=sys.argv
    outdir=root+"/"+args[1]
    argnum=len(args)
    if argnum < 3:
        print("Invalid parameter: [out dir] [dxxnyy/zz] ..")
        sys.exit()
    paralen=argnum-2
    node=["50","100","200","300","500"]

    for arg in range(2, argnum, 1):
        datadir=args[arg]
        datadirsp=datadir.split('/')
        logfile=root+"/"+datadir+"/output/CrystalSi64/training.log"
        outfile= outdir+"/"+datadirsp[0]+"-"+datadirsp[1]+".csv"

        with open(outfile, 'w') as f1:
            writer = csv.writer(f1, lineterminator='\n')

            with open(logfile, 'r') as f2:
                logdata= f2.read()
                listdata= ast.literal_eval(logdata)
                listlen= len(listdata)
                for epc in range(9, listlen, 10):
                    outdata=[]
                    epcdata=listdata[epc]
                    outdata.append(int(epcdata["epoch"]))
                    tf=float(epcdata["main/RMSE/force"])
                    vf=float(epcdata["val/main/RMSE/force"])
                    diff=vf-tf
                    outdata.append(tf)
                    outdata.append(vf)
                    outdata.append(diff)
                    writer.writerow(outdata)
            


"""
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
"""