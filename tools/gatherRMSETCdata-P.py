# -*- coding: utf-8 -*-
import os
import csv
import ast
from itertools import islice
import matplotlib.pyplot as plt

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
    os.makedirs(root+"/result/traincv/plot")
    os.makedirs(root+"/result/grpplot")
    traindir=root+"/result/traincv/"
    plotdir=root+"/result/grpplot/"
    labels=('dif>5','5>dif>3','3>dif>1','1>dif>-1','-1>dif>-3','-3>dif>-5','-5>dif')
    colors=("b","c","cyan","k","yellow","orange","red")
    
    with open(rstfile, 'w') as rslt:
        writer1 = csv.writer(rslt, lineterminator='\n')
        for k in tdata:
            for i in node:
                grpname="d"+k+"n"+i
                print(grpname)
                vfp=[]
                TCerrp=[]
                diffavep=[]
                grpplotfile=plotdir+grpname+".png"
                
                for j in range(1, 11):
                    dataname=grpname+"-"+str(j)
                    logfile= root+"/d"+k+"n"+i+"/"+str(j)+"/output/CrystalSi64/training.log"
                    traincvfile= traindir+dataname+".csv"
                    plotfile= traindir+"/plot/"+dataname+".png"

                    with open(logfile, 'r') as log:
                        logdata= log.read()
                        listdata= ast.literal_eval(logdata)
                        listlen= len(listdata)
                        diffnum=0
                        difftotal=0
                        epl=[]
                        tfl=[]
                        vfl=[]
                        diffl=[]
                        with open(traincvfile, 'w') as tcv:
                            writer2 = csv.writer(tcv, lineterminator='\n')
                            for epc in range(9, listlen, 10):
                                ep=int(listdata[epc]["epoch"])
                                tf=float(listdata[epc]["main/RMSE/force"])*1000
                                vf=float(listdata[epc]["val/main/RMSE/force"])*1000
                                diff=vf-tf
                                outdata=[ep]+[tf]+[vf]+[diff]
                                writer2.writerow(outdata)
                                epl.append(ep)
                                tfl.append(tf)
                                vfl.append(vf)
                                diffl.append(diff)
                                if epc > listlen-200:
                                    diffnum=diffnum+1
                                    difftotal=difftotal+diff
                            diffave=difftotal/diffnum
                            vfp.append(vf)
                            if diffave>5:
                                diffavep.append(0)
                            elif diffave>3:
                                diffavep.append(1)
                            elif diffave>1:
                                diffavep.append(2)
                            elif diffave>-1:
                                diffavep.append(3)
                            elif diffave>-3:
                                diffavep.append(4)
                            elif diffave>-5:
                                diffavep.append(5)
                            else:
                                diffavep.append(6)
                                
                        # Plotting Training curve and diff of Train&Validation
                        # Axis-1: ax1 for Train and Validation
                        # Axis-2: ax2 for difference of Train and Validation
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111)
                        ln1 = ax1.plot(epl, tfl, color="blue", label="Train")
                        ln2 = ax1.plot(epl, vfl, color="red", label="Validation")
                        ax2 = ax1.twinx()  # convining ax1 and ax2
                        ln3 = ax2.plot(epl, diffl, color="green", label="Diff")
                        ax2.set_ylim(-28, 22)  # fixing y-axis scale 
                        plt.title(dataname)
                        ax1.set_xlabel('epoch')
                        ax1.set_ylabel('force/RMSE (meV/A)')
                        ax1.grid(True)
                        ax2.set_ylabel('Diff (Val-Trn)')
                        # merging legend of ax1 and ax2
                        handler1, label1 = ax1.get_legend_handles_labels()
                        handler2, label2 = ax2.get_legend_handles_labels()
                        ax1.legend(handler1 + handler2, label1 + label2, loc=2)
                        plt.savefig(plotfile)
                    
                    infile =root+"/d"+k+"n"+i+"/"+str(j)+"/predict-phono3py/out.txt"
                    with open(infile, 'r') as infl:
                        for n, line in enumerate(infl):
                            if 'Thermal conductivity (W/m-k)' in line:
                                infl.seek(0)
                                for lined in islice(infl, n+32, n+33):
                                     data=lined.split()
                                     TCerr=abs(float(data[1])-112.1)

                    RMSEdt=[dataname]+[vf]+[diffave]+[TCerr]
                    writer1.writerow(RMSEdt)
                    TCerrp.append(TCerr)
                    
                #Plotting correlation of force/RMSE and TC error for each group
                fig = plt.figure()
                ax3 = fig.add_subplot(111)
                plt.title(grpname)
                ax3.set_xlabel("TC Err (fm 112.1)")
                ax3.set_ylabel("force/RMSE (meV/A)")
                ax3.grid(True)
                plt.rcParams["legend.edgecolor"] ='green'
                for j in range(0, 10):
                    lbl=labels[diffavep[j]]
                    clr=colors[diffavep[j]]
                    ax3.scatter(TCerrp[j],vfp[j],c=clr,marker='o',label=lbl)
                left, right = ax3.get_xlim()
                ax3.set_xlim(-0.1, right*1.2)
                #ax4 is only for plotting legend of all kind of data
                ax4 = ax3.twinx()
                for j in range(0, 7):
                    lbl=labels[j]
                    clr=colors[j]
                    ax4.scatter(TCerrp[0],vfp[0],c=clr,marker='o',label=lbl)
                handler4, label4 = ax4.get_legend_handles_labels()
                ax3.legend(handler4, label4,loc='upper right',title='dif=Val-Train',bbox_to_anchor=(0.97, 0.85, 0.14, .100),borderaxespad=0.,)
                fig.delaxes(ax4)
                plt.savefig(grpplotfile)
