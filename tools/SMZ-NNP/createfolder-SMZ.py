# coding: utf-8
import shutil,os

"""
This script is for creating folder of LAMMPS-MD 1000Kmix7
with copying mixed 700 sample xyz from /datas/1000K-LC7/mix
"""

if __name__ == '__main__': 
    folders=['Lin', 'smz']
    SMZroot="/home/okugawa/NNP-F/SMZ-200721/"

    for fld in folders:
        #create data folders
        trnfld=SMZroot+"training_1element-"+fld+"sf/"
        maxminfolder=trnfld+"data_maxmin"

        for j in range(1,11):
            flddstn = trnfld+str(j)+"/"
            shutil.copytree(maxminfolder, flddstn+"data_maxmin")
            os.makedirs(flddstn+"data_weight")
            shutil.copy2(trnfld+"input_tag_training.dat", flddstn)
            shutil.copy2(trnfld+"maxmin_sf/input_nnp.dat", flddstn)
            shutil.copy2(trnfld+"a.out", flddstn)
            shutil.copy2(trnfld+"run.csh", flddstn)
            
            print(f'Create /training_1element-{fld}/{str(j)} data folder')