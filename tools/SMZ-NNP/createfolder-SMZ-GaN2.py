# coding: utf-8
import shutil
import os

"""
This script is for creating folder of CrystalGa16N16 for SMZ-NNP with
data_nnp converted from sample50.xyz(1750smpl) & sample100.xyz(3500smpl) data
"""

def fileEdit1(fname):
    index1= 'dir_data = "../step2_data_binary/data"'
    text1= 'dir_data = "../../step2_data_binary/data"\n'
    index2= 'dir_sf   = "../step3_sf/data_sf/rc_7"'
    text2= 'dir_sf   = "../../step3_sf/data_sf/rc_7"\n'
    
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
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/"
    grps=["1750smpl","3500smpl"]
    
    for grp in grps:
        trfolder=GaNfolder+grp+"/training_2element/"

        #create data folders
        maxminorgin = trfolder+"data_maxmin"
        aoutorgin = trfolder+"a.out"
        inpnnporgin = trfolder+"input_nnp.dat"
        inptagorgin = trfolder+"input_tag_training.dat"
        runorgin = trfolder+"run.csh"
        
        for i in range(1,11):
            wkfolder=trfolder+str(i)
            weightfld = wkfolder+"/data_weight"
            
            shutil.copytree(maxminorgin, wkfolder+"/data_maxmin")
            os.makedirs(weightfld)
            shutil.copy2(aoutorgin, wkfolder)
            shutil.copy2(inpnnporgin, wkfolder)
            shutil.copy2(inptagorgin, wkfolder)
            shutil.copy2(runorgin, wkfolder)
            fileEdit1(wkfolder+"/input_nnp.dat")
                
            print(f'Create /GaN/SMZ-200901/{grp}/training_2element/{str(i)} data folder')