# coding: utf-8
import shutil
import os

"""
This script is for creating poscar_elm2 folder of CrystalGa16N16
 1750smpl & 3500smpl for SMZ-NNP
"""

if __name__ == '__main__': 
    GaNfolder="/home/okugawa/NNP-F/GaN/SMZ-200901/"
    ph3scrbase="/home/okugawa/NNP-F/GaN/GaN-shimizuNNP/"
    grps=["1750smpl","3500smpl"]
    
    for grp in grps:
        trfolder=GaNfolder+grp+"/training_2element/"

        #Copied folders and files
        aoutorgin = trfolder+"poscar_elm2_new/a.out"
        inpnnporgin = trfolder+"poscar_elm2_new/input_nnp.dat"
        paramorgin = trfolder+"poscar_elm2_new/param_nnp.dat"
        
        scrptorgin = ph3scrbase+"phono3py_shimizuNNP.py"
        cnfgorgin = ph3scrbase+"phono3py_config.yaml"
        pscorgin = ph3scrbase+"POSCAR"
        
        for i in range(1,11):
            trifolder=trfolder+str(i)
            wkfolder=trifolder+"/poscar_elm2"
            maxminorgin = trifolder+"/data_maxmin"
            weightorgin = trifolder+"/data_weight"
            
            os.makedirs(wkfolder)
            shutil.copytree(maxminorgin, wkfolder+"/data_maxmin")
            shutil.copytree(weightorgin, wkfolder+"/data_weight")
            shutil.copy2(aoutorgin, wkfolder)
            shutil.copy2(inpnnporgin, wkfolder)
            shutil.copy2(paramorgin, wkfolder)
            shutil.copy2(scrptorgin, wkfolder)
            shutil.copy2(cnfgorgin, wkfolder)
            shutil.copy2(pscorgin, wkfolder)

            print(f'Create /{grp}/training_2element/{str(i)}/poscar_elm2 folder')