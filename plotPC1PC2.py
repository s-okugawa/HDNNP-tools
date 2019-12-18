# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

"""
This script is for plotting PCx data and PC1/PC2 scattering
after PCA and shuffle which is loaded from preprocd_dataset.npz
"""

if __name__ == '__main__': 
    root=os.getcwd()
    dtsetfile=root+"/data/CrystalSi64/preprocd_dataset.npz"
    plotdir=root+"/result/"
    
    dtset= np.load(dtsetfile, allow_pickle=True)
    #allow_pickle op is for adapting spec change of numpy 1.16.3 and later
    dts= dtset['dataset']
    dataset0=[]

    for dt in dts:
        dt0=dt['inputs/0']
        dataset0.append(dt0)

    dim0=len(dataset0)
    dim1=len(dataset0[0])
    dim2=len(dataset0[0][0])
    print(f'Shape of dataset0= {dim0} x {dim1} x {dim2}')

### plot heatmap of one sample of inputs/0
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    xlb=[]
    ylb=[]
    for i in range(1, 42):
        xlb.append("PC"+str(i))
    for i in range(1, 65):
        ylb.append("A"+str(i))

    smpl1=dataset0[0]  ## Pick up sample No.1
    df=pd.DataFrame(data=smpl1, index=ylb, columns=xlb)
    fig, ax1 = plt.subplots(figsize=(12, 9)) 
    sns.heatmap(df, cmap='tab20')
    plt.title("CrystalSi64 PCx data after shuffle")
    plotfile1=plotdir+"Dataset0-data1.png"
    plt.savefig(plotfile1)
    plt.close()

### plot scatter of inputs/0 PC1&PC2
    fig = plt.figure()
    ax2 = fig.add_subplot(111)
    plt.title("CrystalSi64 PC1 & PC2 of inputs/0")

    ax2.set_xlabel("PC1")
    ax2.set_ylabel("PC2")
    ax2.grid(True)
                
    for dt in dataset0:
        dtt=dt.T
        ax2.scatter(dtt[0],dtt[1],marker='.')
    plotfile2=plotdir+"Dataset0-PC1PC2.png"
    plt.savefig(plotfile2)
    plt.close() 
