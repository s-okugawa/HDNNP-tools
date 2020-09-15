# coding: utf-8
import shutil,os

"""
This script is for creating folder of LAMMPS-MD 1000Kmix7
with copying mixed 700 sample xyz from /datas/1000K-LC7/mix
"""
## Modifying xyz data file name of TrainingConfig.py
def fileEdit(fname):
    index1= 'alpha = 0.20d0'
    index2= 'beta  = 0.80d0'
    text1= "alpha = 0.50d0    # loss function ratio: energy\n"
    text2= "beta  = 0.50d0    # loss function ratio: force\n"

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
    folders=['Lin', 'smz']
    SMZroot="/home/okugawa/NNP-F/SMZ-200721/"

    for fld in folders:
        #create data folders
        trnfld=SMZroot+"training_1element-"+fld+"sf/"
        maxminfolder=trnfld+"data_maxmin"

        for j in range(11,21):
            flddstn = trnfld+str(j)+"/"
            shutil.copytree(maxminfolder, flddstn+"data_maxmin")
            os.makedirs(flddstn+"data_weight")
            shutil.copy2(trnfld+"input_tag_training.dat", flddstn)
            shutil.copy2(trnfld+"maxmin_sf/input_nnp.dat", flddstn)
            fileEdit(flddstn+"input_nnp.dat")
            shutil.copy2(trnfld+"a.out", flddstn)
            shutil.copy2(trnfld+"run.csh", flddstn)
            
            print(f'Created /training_1element-{fld}/{str(j)} data folder')