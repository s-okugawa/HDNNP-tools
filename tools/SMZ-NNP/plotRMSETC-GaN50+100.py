# coding: utf-8
import matplotlib.pyplot as plt
import csv
import sys
from itertools import islice

"""
This script is for gathering force/RMSE data and Thermal conductivity data
 of GaN 1750&3500 sample and plot them
"""

if __name__ == '__main__': 
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/"
    rmsefile=GaNfolder+"result/RMSE50+100.csv"
    rmseTCfile=GaNfolder+"result/RMSETC50+100.csv"
    pltfile=GaNfolder+"result/RMSETC50+100.png"
    grps=["1750","3500"]
    colors=["red","b"]
    
    rmsedt, rmseTCdt = [],[]

    #Read force/RMSE of 1750&3500sample data from RMSE.csv
    with open(rmsefile, 'r') as rmsef:
        reader = csv.reader(rmsef)
        for row in reader:
            rmsedt.append([row[0],float(row[7])])
            
    #Read TC of 1750&3500sample data from poscar-elm2/out.txt
    TCdt=[]
    for grp in grps:
        for i in range(1,11):
            grpname=grp+"smpl-"+str(i)
            TCfolder =GaNfolder+grp+"smpl/training_2element/"+str(i)
            TCfile= TCfolder+"/poscar_elm2/out.txt"
        
            with open(TCfile, 'r') as TCf:
                for n, line in enumerate(TCf):
                    if 'Thermal conductivity (W/m-k)' in line:
                        TCf.seek(0)
                        for lined in islice(TCf, n+32, n+33):
                            data=lined.split()
                            if data[0]!="300.0":
                                print(f'TC read error: [{data[0]}]K data is read')
                                sys.exit()
                            TCdt.append([grpname,float(data[1])])
                            
    #Merge force/RMSE & TC data
    for j,rm in enumerate(rmsedt):
        if rm[0]!=TCdt[j][0]:
            print(f'RMSE & TC append error: RMSE={rm[0]}, TC={TCdt[j][0]}')
            sys.exit()
        else:
            rmseTCdt.append([rm[0],rm[1],TCdt[j][1]])

    #Write force/RMSE & TC data to csv
    with open(rmseTCfile, 'w') as rtcv:
        writer2 = csv.writer(rtcv, lineterminator='\n')
        for rmtc in rmseTCdt:
            writer2.writerow(rmtc)
            
    #Plotting force/RMSE and TC of each sample
    L1, L2 = 0, 0
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title("[GaN 1750 & 3500 sample] force/RMSE & TC")
    ax1.set_xlabel("Thermal Conductivity (W/m-K:300K)")
    ax1.set_ylabel("force/RMSE (meV/ang)")
    ax1.grid(True)
    plt.rcParams["legend.edgecolor"] ='green'
    for rmtc in rmseTCdt:
        if "1750smpl" in rmtc[0]:
            clr="red"
            L1+=1
        elif "3500smpl" in rmtc[0]:
            clr="b"
            L2+=1
        else:
            print(f'RMSE & TC data header error: "{rmtc[0]}"')
            sys.exit()
        ax1.scatter(rmtc[2],rmtc[1],c=clr,marker='.')

    left, right = ax1.get_xlim()
    ax1.set_xlim(left, right*1.03)

    #ax2 is only for plotting legend of all kind of data
    ax2 = ax1.twinx()
    for k,grp in enumerate(grps):
        ax2.scatter(rmtc[2],rmtc[1],c=colors[k],marker='.',label=grp)
    handler2, label2 = ax2.get_legend_handles_labels()
    ax1.legend(handler2, label2,loc='upper right',title='Samples')
    fig.delaxes(ax2)
    plt.savefig(pltfile)
    print(f'force/RMSE & TC of 1750smpl({L1}) & 3500smpl({L2}) are plotted')
    plt.close()