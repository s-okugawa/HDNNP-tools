# -*- coding: utf-8 -*-
import os, sys
import shutil

"""
This script is creating folder of Train and Phonopy, Phono3py by
copying seed folder and modifying TrainingConfig and Phono(3)pyPrep of each.
Seed folder must be existed in [current dir]/dxxn50/1 in advance
 
Usage:
$ python creatednfolder.py [d1], [d2] ...
 [d1], [d2] ...: number of training data like as 5, 10, 20
"""

## Modifying node# and xyz data file name of TrainingConfig.py
def fileEdit1(fname, k, i):
    index1= "'tanh')"
    index2= 'c.TrainingConfig.data_file ='
    text1= "   ("+i+", 'tanh'),\n"
    text2= "c.TrainingConfig.data_file = './data/all"+str(k)+".xyz'\n"

    with open(fname, 'r') as infl:
        tmp_list =[]
        for row in infl:
            if row.find(index1) != -1:
                tmp_list.append(text1)
            elif row.find(index2) != -1:
                tmp_list.append(text2)
            else:
                tmp_list.append(row)

    with open(fname, 'w') as f2:
        for ii in range(len(tmp_list)):
            f2.write(tmp_list[ii])

## Modifying output directory name of phonopyPrep.py and phono3pyPrep.py
def fileEdit2(fname, root, k, i, j):
    index= 'nnpout='
    text= "nnpout='"+root+"/d"+str(k)+"n"+i+"/"+str(j)+"/output'\n"

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

    args=sys.argv
    argnum=len(args)
    if argnum < 2:
        print("Invalid parameter: at least 1 data# parameter is needed")
        sys.exit()
    paralen=argnum-1
    node=["50","100","200","300","500"]

    for arg in range(1, argnum, 1):
        k=args[arg]

        for i in node:
            dirorg = root+"/d"+str(k)+"n"+node[0]+"/1"
            dirdest = root+"/d"+str(k)+"n"+i+"/1"
            if i != node[0]:
                shutil.copytree(dirorg, dirdest)
            for j in range(1, 11):
                dirorg = root+"/d"+str(k)+"n"+i+"/1"
                dirdest = root+"/d"+str(k)+"n"+i+"/"+str(j)
                if j != 1:
                    shutil.copytree(dirorg, dirdest)  ## copy seed dir
                trncnffname = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/training_config.py"
                fileEdit1(trncnffname, k, i)
                fname1 = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phonopy/phonopyPrep.py"
                fname2 = root+"/d"+str(k)+"n"+i+"/"+str(j)+"/predict-phono3py/phono3pyPrep.py"
                fileEdit2(fname1, root, k, i, j)
                fileEdit2(fname2, root, k, i, j)
             