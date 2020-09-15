# coding: utf-8
import shutil
import os

"""
This script is for creating folder of Si-amorphous for SMZ-NNP
with data_nnp converted from sample225+10.xyz data
"""

if __name__ == '__main__': 
    amr471folder="/home/okugawa/NNP-F/SMZ-amr/training_1element/471smpl/"

    #create data folders
    maxminorgin = amr471folder+"data_maxmin"
    aoutorgin = amr471folder+"a.out"
    inpnnporgin = amr471folder+"input_nnp.dat"
    inptagorgin = amr471folder+"input_tag_training.dat"
    runorgin = amr471folder+"run.csh"
    
    for i in range(1,11):
        wkfolder=amr471folder+str(i)
        weightfld = wkfolder+"/data_weight"
        
        shutil.copytree(maxminorgin, wkfolder+"/data_maxmin")
        os.makedirs(weightfld)
        shutil.copy2(aoutorgin, wkfolder)
        shutil.copy2(inpnnporgin, wkfolder)
        shutil.copy2(inptagorgin, wkfolder)
        shutil.copy2(runorgin, wkfolder)
            
        print(f'Create NNP-F/SMZ-amr/training_1element/471smpl/{str(i)} data folder')