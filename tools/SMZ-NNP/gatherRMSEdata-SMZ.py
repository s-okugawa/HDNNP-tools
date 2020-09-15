# -*- coding: utf-8 -*-
import csv
import sys
import math
import matplotlib.pyplot as plt

"""
This script is made to output csv file by gathering 
train curve data (epoch, energy & force of train & test)
from mse_training.dat and mse_test.dat of training_1element of Shimizu-san NNP
And plot train curve and scatter of force/RMSE&TC data
"""

def gatherplot(mtrainfile,mtestfile,traincvfile,plotfile,dataname):
    rmse=[[] for i in range(5)]
    outdata=[]
    with open(mtrainfile,'r') as mtr, open(mtestfile,'r') as mts:
        iter=1
        for line in mtr:
            if not "#" in line:
                if iter % 10 ==0:
                    data=line.split()
                    tre=math.sqrt(float(data[0]))*1000
                    trf=math.sqrt(float(data[1]))*1000
                    rmse[0].append(iter)
                    rmse[1].append(tre)
                    rmse[3].append(trf)
                    outdata.append([iter,tre,trf])
                iter+=1

        iter=1
        for line in mts:
            if not "#" in line:
                if iter % 10 ==0:
                    data=line.split()
                    tse=math.sqrt(float(data[0]))*1000
                    tsf=math.sqrt(float(data[1]))*1000
                    rmse[2].append(tse)
                    rmse[4].append(tsf)
                    itern= iter // 10
                    outdata[itern-1].insert(2,tse)
                    outdata[itern-1].insert(4,tsf)
                iter+=1
                
        if len(rmse[0]) != len(rmse[2]):
            print(f'Error: length of train= {len(rmse[0])} & test= {len(rmse[1])}')
            sys.exit()            
                    
    #Write out RMSE datas to csv file
    with open(traincvfile, 'w') as tcv:
        writer2 = csv.writer(tcv, lineterminator='\n')
        for csvdata in outdata:
            writer2.writerow(csvdata)
                    
    # Plotting Training curve and diff of Train&Validation
    # Axis-1: ax1 for RMSE of energy
    # Axis-2: ax2 for RMSE of force
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ln1 = ax1.plot(rmse[0], rmse[1], color="orange", label="Energy(Train)")
    ln2 = ax1.plot(rmse[0], rmse[2], color="red", label="Energy(Test)")
    ax1.set_ylim(-2, 20)  # fixing y-axis scale
    ax2 = ax1.twinx()  # convining ax1 and ax2
    ln3 = ax2.plot(rmse[0], rmse[3], color="green", label="Force(Train)")
    ln4 = ax2.plot(rmse[0], rmse[4], color="blue", label="Force(Test)")
    ax2.set_ylim(0, 200)  # fixing y-axis scale
    ttl = "["+dataname+"] Training curve of Energy & Force"
    plt.title(ttl)
    ax1.set_xlabel('iterate')
    ax1.set_ylabel('Energy/RMSE (meV/atom)')
    ax1.grid(True)
    ax2.set_ylabel('Force/RMSE (meV/ang)')
    # merging legend of ax1 and ax2
    handler1, label1 = ax1.get_legend_handles_labels()
    handler2, label2 = ax2.get_legend_handles_labels()
    ax1.legend(handler1 + handler2, label1 + label2, loc="upper right")
    plt.savefig(plotfile)
    plt.close()
            
if __name__ == '__main__': 
    SMZfolder="/home/okugawa/NNP-F/SMZ-200721/"
    traincvdir=SMZfolder+"result/traincv/"
    plotdir=traincvdir+"plot/"
    grps=["Lin", "smz"]
    
    for grp in grps:
        trnfolder=SMZfolder+"training_1element-"+grp+"sf/"
        for i in range(1,21):
            mtrainfile=trnfolder+str(i)+"/mse_training.dat"
            mtestfile=trnfolder+str(i)+"/mse_test.dat"
            dataname=grp+"-"+str(i)
            traincvfile=traincvdir+dataname+".csv"
            plotfile=plotdir+dataname+".png"
            gatherplot(mtrainfile,mtestfile,traincvfile,plotfile,dataname)
            
            print(f'SMZ-200721/{dataname} is gathered and plotted')