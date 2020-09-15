# coding: utf-8
import shutil
import os

"""
This script is for creating folder of CrystalGa16N16 for SMZ-NNP
with data_nnp converted from sample10.xyz data
"""

def fileEdit1(fname):
    index1= 'dir_data = "../step2_data_binary/data"'
    text1= 'dir_data = "../../../step2_data_binary/data"\n'
    index2= 'dir_sf   = "../step3_sf/data_sf/rc_7"'
    text2= 'dir_sf   = "../../../step3_sf/data_sf/rc_7"\n'
    
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

if __name__ == '__main__': 
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/training_2element/"

    #create data folders
    maxminorgin = GaNfolder+"data_maxmin"
    aoutorgin = GaNfolder+"a.out"
    inpnnporgin = GaNfolder+"input_nnp.dat"
    inptagorgin = GaNfolder+"input_tag_training.dat"
    runorgin = GaNfolder+"run.csh"
    
    for i in range(1,11):
        wkfolder=GaNfolder+"350smpl/"+str(i)
        weightfld = wkfolder+"/data_weight"
        
        shutil.copytree(maxminorgin, wkfolder+"/data_maxmin")
        os.makedirs(weightfld)
        shutil.copy2(aoutorgin, wkfolder)
        shutil.copy2(inpnnporgin, wkfolder)
        shutil.copy2(inptagorgin, wkfolder)
        shutil.copy2(runorgin, wkfolder)
        fileEdit1(wkfolder+"/input_nnp.dat")
            
        print(f'Create NNP-F/GaN/SMZ-200901/training_2element/350smpl/{str(i)} data folder')