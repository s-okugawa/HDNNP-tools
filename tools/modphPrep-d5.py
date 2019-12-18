# -*- coding: utf-8 -*-
import os, sys

if __name__ == '__main__': 
    root=os.getcwd()
    slh=' \\'
    index= '#$ -pe smp 24'
    text= '    pr.write("#$ -pe x24 24'+slh+'n")\n'

    node=["50", "100", "200", "300", "500"]
    k=5
    for i in node:
        for j in range(1, 11):
            fname = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phono3py/phono3pyPrep.py"
            with open(fname, 'r') as infl:
                tmp_list =[]
                for row in infl:
                    if row.find(index) != -1:
                        tmp_list.append(text)
                    else:
                        tmp_list.append(row)

            with open(fname, 'w') as f2:
                for ii in range(len(tmp_list)):
                    f2.write(tmp_list[ii])
