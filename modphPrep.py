# -*- coding: utf-8 -*-
import os, sys

def fileEdit(fname, k, i, j):
    index= 'nnpout='
    text= "nnpout='/home/okugawa/HDNNP/Si-190808/d"+str(k)+"n"+i+"/"+str(j)+"/output'\n"

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

if __name__ == '__main__': 
    root=os.getcwd()
    node=["50", "100", "200", "300", "500"]

    for k in range(20, 110, 20):
        for i in node:
             for j in range(6, 11):
                fname1 = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phonopy/phonopyPrep.py"
                fname2 = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phono3py/phono3pyPrep.py"
                fileEdit(fname1, k, i, j)
                fileEdit(fname2, k, i, j)
