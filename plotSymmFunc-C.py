# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

"""
This script is for plotting G1/G2/G4 data of each atom 
by color bar
"""

if __name__ == '__main__': 
    root=os.getcwd()
    symfuncfile=root+"/data/CrystalSi64/symmetry_function.npz"
    plotdir=root+"/result/"
    dngrp=["d2"]
    
    xlb=["G1"]
    ylb=[]
    for i in range(1, 25):
        xlb.append("G2-"+str(i))
    for i in range(1, 17):
        xlb.append("G4-"+str(i))
    for i in range(1, 65):
        ylb.append("A"+str(i))

    symf= np.load(symfuncfile)
    symdata= symf['sym_func']

    smpl0=symdata[10]
    df=pd.DataFrame(data=smpl0, index=ylb, columns=xlb)
    
    fig, ax = plt.subplots(figsize=(12, 9)) 
    sns.heatmap(df, cmap='tab20')
    plt.title("CrystalSi64 Symmetry_Function G1/G2/G4 data")
                  
    plotfile=plotdir+"Gdata-C4.png"
    plt.savefig(plotfile)
    plt.close()