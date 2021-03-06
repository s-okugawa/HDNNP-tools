# -*- coding: utf-8 -*-
import os
import numpy as np

"""
This script is for outputting PC1/PC2/PC3 data from preprocd_dataset.npz
of all bs samples
"""

def makePC123(dtsetfile, outfile, grpname):
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
    
    with open(outfile, 'w') as f1:
        for dt64 in dataset0:
            for dt in dt64:
                wdt=str(dt[0])+" "+str(dt[1])+" "+str(dt[2])+"\n"
                f1.write(wdt)
                
    print(f'Saved PC1/PC2/PC3 data of {grpname}: Shape= {dim0} x {dim1} x {dim2}')

if __name__ == '__main__': 
    root=os.getcwd()
    bsxs=["bs1","bs2","bs3","bs4","bs5","bs6","bs7","bs8"]
    outdir=root+"/result/PC123/"

    for bsx in bsxs:
        for j in range(1,11):
            grpname=bsx+"-"+str(j)
            dtsetdir=root+"/"+bsx+"-d20n50/"+str(j)
            dtsetfile=dtsetdir+"/data/CrystalSi64/preprocd_dataset.npz"
            outfile=outdir+grpname+"-PC123.txt"
            makePC123(dtsetfile, outfile, grpname)