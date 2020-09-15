# coding: utf-8
import matplotlib.pyplot as plt
import csv

"""
This script is for gathering force/RMSE data from training result of
GaN 350 sample and plot them
"""

if __name__ == '__main__': 
    GaN350folder="/home/okugawa/NNP-F/GaN/SMZ-200901/training_2element/350smpl/"
    outfile=GaN350folder+"result/RMSE.csv"
    pltfile=GaN350folder+"result/fRMSE.png"
    pltdata=[[] for i in range(10)]
    
    with open(outfile, 'w') as outf:
        writer1 = csv.writer(outf, lineterminator='\n')
        
        for i in range(1,21):
            testjobfile= GaN350folder+str(i)+"/testjob.dat"
            with open(testjobfile, 'r') as testjob:
                for line in testjob:
                    if "Total number of data:" in line:
                        totnum=int(line.split()[4])
                    elif "Number of training data:" in line:
                        trnum=int(line.split()[4])
                    elif "Number of test data:" in line:
                        tsnum=int(line.split()[4])
                    elif "# RMSE of training:" in line:
                        if "eV/atom" in line:
                            etrn=float(line.split()[4])*1000
                        elif "eV/ang" in line:
                            ftrn=float(line.split()[4])*1000
                    elif "# RMSE of test:" in line:
                        if "eV/atom" in line:
                            etstdt=line.split()[4]
                            if etstdt=="NaN":
                                etst=etstdt
                            else:
                                etst=float(etstdt)*1000
                        elif "eV/ang" in line:
                            ftstdt=line.split()[4]
                            if ftstdt=="NaN":
                                ftst=ftstdt
                            else:
                                ftst=float(ftstdt)*1000
                                if i<11:
                                    pltdata[i-1].append(ftst)
                                else:
                                    pltdata[i-11].append(ftst)
                            
            wrdata= [i,totnum,trnum,tsnum,etrn,ftrn,etst,ftst]
            writer1.writerow(wrdata)
    
    #Plot force/RMSE data
    xlbl=["2:8","5:5"]
    clr=["b","green"]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title("GaN 350sample force/RMSE")
    ax1.set_xlabel("Loss-F Energy:Force")
    ax1.set_ylabel("force/RMSE (meV/ang)")
    ax1.grid(True)
    for j in range(10):
        ax1.scatter(xlbl,pltdata[j],c=clr,marker='.')
    plt.savefig(pltfile)
    plt.close()