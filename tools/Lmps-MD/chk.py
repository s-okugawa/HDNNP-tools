# -*- coding: utf-8 -*-
import numpy as np

"""

"""

def chkerr(LC7root, grps, md):
    for grp in grps:
        print(f'Check {md}-{grp}')
        if grp=='mix':
            for i in range(1,10):
                for j in range(1,10):
                    datadir=LC7root+grp+"/"+str(i)+"/"+str(j)
                    symfft=datadir+"/data/CrystalSi64/symmetry_function.npz"
                    symt= np.load(symfft)
                    st= symt['sym_func']
                    symffp=datadir+"/predict-phono3py-2/output-phono3py/symmetry_function-pred.npz"
                    symp= np.load(symffp)
                    sp= symp['sym_func']
                    if not len(st)==630 and len(st[0])==64 and len(st[0][0])==41:
                        print(f'{md} Train of {grp}/{i}/{j} is {len(st)}x{len(st[0])}x{len(st[0][0])}')
                    if not len(sp)==111 and len(sp[0])==64 and len(sp[0][0])==41:
                        print(f'{md} Pred of {grp}/{i}/{j} is {len(sp)}x{len(sp[0])}x{len(sp[0][0])}')
                        #errfile=LC7root+"chkerr/"+grp+"-"+str(i)+"-"+str(j)+".txt"
                        #np.savetxt(errfile,sp)
                            
        else:
            for j in range(1,10):
                datadir=LC7root+grp+"/"+str(j)
                symfft=datadir+"/data/CrystalSi64/symmetry_function.npz"
                symt= np.load(symfft)
                st= symt['sym_func']
                symffp=datadir+"/predict-phono3py-2/output-phono3py/symmetry_function-pred.npz"
                symp= np.load(symffp)
                sp= symp['sym_func']
                if not len(st)==630 and len(st[0])==64 and len(st[0][0])==41:
                    print(f'{md} Train of {grp}/{j} is {len(st)}x{len(st[0])}x{len(st[0][0])}')
                if not len(sp)==111 and len(sp[0])==64 and len(sp[0][0])==41:
                    print(f'{md} Pred of {grp}/{j} is {len(sp)}x{len(sp[0])}x{len(sp[0][0])}')
                    #errfile=LC7root+"chkerr/"+grp+"-"+str(j)+".txt"
                    #np.savetxt(errfile,sp)
                                
if __name__ == '__main__': 
    #calculate the diff of Lammps-MD LC7 Symm_Func of Train & Predict
    LC7root="/home/okugawa/HDNNP/Si-190808/1000K-LC7/"
    grps=['0.95','0.97','0.99','1.00','1.01','1.03','1.05','mix']
    chkerr(LC7root, grps,"Lammps-MD")
    
    #calculate the diff of AIMD LC7 Symm_Func of Train & Predict
    LC7root="/home/okugawa/HDNNP/Si-190808-md/1000K-LC7n/"
    grps=['0.95','0.97','0.99','1.0','1.01','1.03','1.05','mix']
    chkerr(LC7root, grps,"AIMD")    