# -*- coding: utf-8 -*-
import os
import numpy as np

"""
This script is for outputting PC1/PC2/PC3 data from preprocd_dataset.npz
"""

if __name__ == '__main__': 
    root=os.getcwd()
    dtsetfile=root+"/data/CrystalSi64/preprocd_dataset.npz"
    outfile=root+"/result/PC123.txt"

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
    
    with open(outfile, 'w') as f1:
        for dt64 in dataset0:
            for dt in dt64:
                wdt=str(dt[0])+" "+str(dt[1])+" "+str(dt[2])+"\n"
                f1.write(wdt)

    print(f'*** End of saving PC1/PC2/PC3 data ***')
