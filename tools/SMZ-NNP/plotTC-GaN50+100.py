# coding: utf-8
import matplotlib.pyplot as plt
import csv
from itertools import islice

"""
This script is for gathering Thermal conductivity data of GaN 1750&3500 sample
 and comparing with DFT result
"""

def plotTC(TCdt,DFTTCdt,OGRTCdt,grp, plotfolder):   #Plotting TC data of each sample
    #Plot each sample with DFT&Ogura-HDNNP result
    for i in range(10):
        smplname=grp+"-"+str(i+1)
        plotfile=plotfolder+smplname+".png"
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        plt.title(f'[SMZ-NNP:GaN {smplname}] Thermal Conductivity')
        ax1.set_xlabel("Temperature (K)")
        ax1.set_ylabel("Thermal Conductivity (W/m-K)")
        ax1.grid(True)
        ax1.set_ylim(0, 700)
        plt.rcParams["legend.edgecolor"] ='green'
        ax1.plot(TCdt[i][0],TCdt[i][1],c="blue",label="SMZ-x/y")
        ax1.plot(TCdt[i][0],TCdt[i][2],c="blue",linestyle="dotted",label="SMZ-z")
        ax1.plot(OGRTCdt[0],OGRTCdt[1],c="red",label="OGR-x/y")
        ax1.plot(OGRTCdt[0],OGRTCdt[2],c="red",linestyle="dotted",label="OGR-z")
        ax1.plot(DFTTCdt[0],DFTTCdt[1],c="black",label="VASP-x/y")
        ax1.plot(DFTTCdt[0],DFTTCdt[2],c="black",linestyle="dotted",label="VASP-z")
        plt.legend(loc="upper right")
        plt.savefig(plotfile)
        plt.close()
    print(f'TC of each sample ({grp}smpl) is plotted')
        
    #Plot TC(x/y) of all sample with DFT&Ogura-HDNNP result
    plotfile=plotfolder+grp+"-xyall.png"
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title(f'[SMZ-NNP:GaN {grp}-all] Thermal Conductivity (x/y)')
    ax1.set_xlabel("Temperature (K)")
    ax1.set_ylabel("Thermal Conductivity (W/m-K)")
    ax1.grid(True)
    ax1.set_ylim(0, 700)
    plt.rcParams["legend.edgecolor"] ='green'
    ax1.plot(TCdt[0][0],TCdt[0][1],c="blue",label="SMZ")
    for i in range(1,10):
        ax1.plot(TCdt[i][0],TCdt[i][1],c="blue")
    ax1.plot(OGRTCdt[0],OGRTCdt[1],c="red",label="OGR")
    ax1.plot(DFTTCdt[0],DFTTCdt[1],c="black",label="VASP")
    ax1.legend(loc="upper right")
    plt.savefig(plotfile)
    plt.close()
    print(f'TC(x/y) of all sample ({grp}smpl) is plotted')

    #Plot TC(z) of all sample with DFT&Ogura-HDNNP result
    plotfile=plotfolder+grp+"-zall.png"
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title(f'[SMZ-NNP:GaN {grp}-all] Thermal Conductivity (z)')
    ax1.set_xlabel("Temperature (K)")
    ax1.set_ylabel("Thermal Conductivity (W/m-K)")
    ax1.grid(True)
    ax1.set_ylim(0, 700)
    plt.rcParams["legend.edgecolor"] ='green'
    ax1.plot(TCdt[0][0],TCdt[0][2],c="blue",label="SMZ")
    for i in range(1,10):
        ax1.plot(TCdt[i][0],TCdt[i][2],c="blue")
    ax1.plot(OGRTCdt[0],OGRTCdt[2],c="red",label="OGR")
    ax1.plot(DFTTCdt[0],DFTTCdt[2],c="black",label="VASP")
    ax1.legend(loc="upper right")
    plt.savefig(plotfile)
    plt.close()
    print(f'TC(z) of all sample ({grp}smpl) is plotted')

if __name__ == '__main__': 
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/"
    DFTTCfile="/home/okugawa/NNP-F/GaN/GaN-shimizuNNP/data111111.dat-vasp"
    OGRTCfile="/home/okugawa/NNP-F/GaN/GaN-shimizuNNP/data111111.dat-ogura"
    DFTcsv="/home/okugawa/NNP-F/GaN/GaN-shimizuNNP/data111111-vasp.csv"
    OGRcsv="/home/okugawa/NNP-F/GaN/GaN-shimizuNNP/data111111-ogura.csv"
    plotfolder=GaNfolder+"result/"
    grps=["1750","3500"]
    colors=["orange","green"]
    
    #Read DFT result TC data
    DFTTCdt=[[] for i in range(3)]
    with open(DFTTCfile, 'r') as DFTTCf, open(DFTcsv, 'w') as Dcsv:
        writer2 = csv.writer(Dcsv, lineterminator='\n')
        lenDFT=0
        for line in DFTTCf:
            data=line.split()
            if '0.0' in data[0] and data[0]!='0.0':
                wrdata=[float(data[0]),float(data[1]),float(data[2]),float(data[3])]
                writer2.writerow(wrdata)
                DFTTCdt[0].append(float(data[0]))
                DFTTCdt[1].append(float(data[1]))
                DFTTCdt[2].append(float(data[3]))
                lenDFT+=1
    print(f'DFT TC data ({lenDFT}) was read')

    #Read Ogura-HDNNP result TC data
    OGRTCdt=[[] for i in range(3)]
    with open(OGRTCfile, 'r') as OGRTCf, open(OGRcsv, 'w') as Ocsv:
        writer2 = csv.writer(Ocsv, lineterminator='\n')
        lenOGR=0
        for line in OGRTCf:
            data=line.split()
            if '0.0' in data[0] and data[0]!='0.0':
                wrdata=[float(data[0]),float(data[1]),float(data[2]),float(data[3])]
                writer2.writerow(wrdata)
                OGRTCdt[0].append(float(data[0]))
                OGRTCdt[1].append(float(data[1]))
                OGRTCdt[2].append(float(data[3]))
                lenOGR+=1
    print(f'Ogura-HDNNP TC data ({lenOGR}) was read')

    #Read TC of 1750&3500sample data from poscar-elm2/out.txt
    TCdt=[[[[],[],[]] for i in range(10)] for j in range(2)]
    for k,grp in enumerate(grps):
        TCdtfolder=GaNfolder+grp+"smpl/training_2element/TCdata/"
        for i in range(1,11):
            grpname=grp+"-"+str(i)
            TCfolder =GaNfolder+grp+"smpl/training_2element/"+str(i)
            TCdtfile=TCdtfolder+grp+"-"+str(i)+".csv"
            TCfile= TCfolder+"/poscar_elm2/out.txt"
        
            with open(TCfile, 'r') as TCf, open(TCdtfile, 'w') as TCdtf:
                writer2 = csv.writer(TCdtf, lineterminator='\n')
                for n, line in enumerate(TCf):
                    if 'Thermal conductivity (W/m-k)' in line:
                        TCf.seek(0)
                        lenSMZ=0
                        for lined in islice(TCf, n+3, n+103):
                            data=lined.split()
                            wrdata=[float(data[0]),float(data[1]),float(data[2]),float(data[3])]
                            writer2.writerow(wrdata)
                            TCdt[k][i-1][0].append(float(data[0]))
                            TCdt[k][i-1][1].append(float(data[1]))
                            TCdt[k][i-1][2].append(float(data[3]))
                            lenSMZ+=1
                        break
            print(f'{grp}-{i} TC data ({lenSMZ}) was read')
                    
    #Plot TC curve of each sample
    for k,grp in enumerate(grps):
        plotTC(TCdt[k],DFTTCdt,OGRTCdt,grp, plotfolder)