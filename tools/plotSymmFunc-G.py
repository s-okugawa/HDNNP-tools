# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np

"""
This script is for plotting G1/G2/G4 data of calculated Symm-Func
"""

if __name__ == '__main__': 
    root=os.getcwd()
    symfuncfile=root+"/data/CrystalSi64/symmetry_function.npz"
    plotdir=root+"/result/"
    dngrp=["d2"]
    
    xlb=["G1"]
    clr=["b"]
    for i in range(1, 25):
        xlb.append("G2-"+str(i))
        clr.append("g")
    for i in range(1, 17):
        xlb.append("G4-"+str(i))
        clr.append("c")

    symf= np.load(symfuncfile)
    symdata= symf['sym_func']

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title("Symmetry_Function G1/G2/G4 data")
    ax.set_ylabel("Value of G")
    ax.grid(True)
              
    for eachsample in symdata:
        for gdata in eachsample:
            ax.scatter(xlb, gdata, c=clr, marker='.')
            
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=90, fontsize=8);
    plotfile=plotdir+"Gdata-all.png"
    plt.savefig(plotfile)
    plt.close()