# coding: utf-8
import matplotlib.pyplot as plt
import csv

"""
This script is for gathering force/RMSE data from training result of
GaN 1750&3500 sample and plot them with 350 sample
"""

if __name__ == '__main__': 
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/"
    RMSE350smpl=GaNfolder+"350smpl/training_2element/350smpl/result/RMSE.csv"
    outfile=GaNfolder+"result/RMSE50+100.csv"
    pltfile=GaNfolder+"result/fRMSE50+100.png"
    grps=["1750smpl","3500smpl"]
    xlbl=["350smpl","1750smpl","3500smpl"]
    
    pltdata=[[] for i in range(10)]

    #Read force/RMSE of 350sample data from 350smpl/RMSE.csv
    with open(RMSE350smpl, 'r') as rmse350:
        reader = csv.reader(rmse350)
        rmsedt = [row for row in reader]
        for i in range(10):
            pltdata[i].append(float(rmsedt[i][7]))

    #Read force/RMSE of 1750&3500sample data from testjob.dat
    with open(outfile, 'w') as outf:
        writer1 = csv.writer(outf, lineterminator='\n')
            
        for grp in grps:
            trnfolder=GaNfolder+grp+"/training_2element/"

            for i in range(1,11):
                testjobfile= trnfolder+str(i)+"/testjob.dat"
                gname=grp+"-"+str(i)
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
                                    pltdata[i-1].append(ftst)
                                
                wrdata= [gname,totnum,trnum,tsnum,etrn,ftrn,etst,ftst]
                writer1.writerow(wrdata)
    
    #Plot force/RMSE data
    clr=["brown","b","green"]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title("GaN 350 & 1750 & 3500 sample force/RMSE")
    ax1.set_ylabel("force/RMSE (meV/ang)")
    ax1.grid(True)
    for j in range(10):
        ax1.scatter(xlbl,pltdata[j],c=clr,marker='.')
    plt.savefig(pltfile)
    plt.close()