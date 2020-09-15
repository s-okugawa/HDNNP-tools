#!/usr/bin/env python
# coding: utf-8
import sys
import random
import pathlib
import os
import numpy as np
from ase.io import read, iread
import shutil
import pprint


"""
This script is to convert xyz file using ogura NNP
for Shimizu-san's HDNNP code
$ python fromxyz-sNNP.py [filename] [tag] [dir]
filename: name of xyz
tag: information of samples
dir : the directory name to store the all file
"""

#copy from ase
def _symbol_count_from_symbols(symbols):
    """Reduce list of chemical symbols into compact VASP notation

    args:
        symbols (iterable of str)

    returns:
        list of pairs [(el1, c1), (el2, c2), ...]
    """
    sc = []
    psym = symbols[0]
    count = 0
    for sym in symbols:
        if sym != psym:
            sc.append((psym, count))
            psym = sym
            count = 1
        else:
            count += 1
    sc.append((psym, count))
    return sc




args = sys.argv
file = args[1]
tag = args[2]
dir = args[3]

os.makedirs(dir, exist_ok=True)
counter = 1

atoms=iread(file,index=':', format='xyz')

# file for make binary data step
with open("input_tag.dat", "w") as tagfile:
    for a in atoms:
        forces = a.get_forces()
        positions = a.get_positions()
        scaled_position=a.get_scaled_positions()
        energy = a.get_total_energy()
        natom = len(forces)
        tagfile.write(tag + str(natom) + "atoms" + "_" + str(counter) + "\n")
        xdatcar=dir + '/positions_' + tag + str(natom) + "atoms" + "_" + str(counter) + ".dat"
        with open(xdatcar, "w") as xdat:
            symbol_count = _symbol_count_from_symbols(a.get_chemical_symbols())
            label = ' '.join([s for s, _ in symbol_count])
            xdat.write(str(label)+"\n")
            xdat.write("1.0 \n")
            xdat.write(str(a.cell[0][0])+" "+str(a.cell[0][1])+" "+str(a.cell[0][2])+"\n")
            xdat.write(str(a.cell[1][0]) + " " + str(a.cell[1][1]) + " " + str(a.cell[1][2]) + "\n")
            xdat.write(str(a.cell[2][0]) + " " + str(a.cell[2][1]) + " " + str(a.cell[2][2]) + "\n")
            for sym, _ in symbol_count:
                xdat.write(' {:3s}'.format(sym))
            xdat.write('\n')
            for _, count in symbol_count:
                xdat.write(' {:3d}'.format(count))
            xdat.write('\n')
            xdat.write("Direct configuration=     1 \n")
            for pos in scaled_position:
                xdat.write(str(pos[0]) + " "+ str(pos[1]) +" "+ str(pos[2]) +"\n")

        with open(dir + '/forces_' + tag + str(natom) + "atoms" + "_" + str(counter) + ".dat", 'w') as out:
            out.write("--\n")
            out.write(" POSITION                                       TOTAL-FORCE (eV/Angst) \n")
            out.write(" ----------------------------------------------------------------------------------- \n ")
            for i, p in enumerate(positions):
                out.write(str(p[0]) + " " + str(p[1]) + " " + str(p[2]) + " " + str(forces[i][0]) + " " + str(
                    forces[i][1]) + " " + str(forces[i][2]) + "\n")
        with open(dir + '/energies_' + tag + str(natom) + "atoms" + "_" + str(counter) + ".dat", 'w') as ene:
            ene.write(str(energy) + "\n")

        # very tentative version
        with open(dir + '/info_' + tag + str(natom) + "atoms" + "_" + str(counter) + ".dat", 'w') as info:
            symbol_count = _symbol_count_from_symbols(a.get_chemical_symbols())
            info.write("\n")
            info.write("Total_number_of_ions " + str(natom) + "\n")
            info.write("\n")
            info.write("Ions_per_type " +str(len(symbol_count))+  "\n")
            info.write("\n")
            for sym, count in symbol_count:
                info.write('{:3s}'.format(sym) + ' {:3d}'.format(count) + "\n")
            info.write("\n")
            info.write("MD_steps 1 \n")
            
        print(counter)
        counter = counter + 1

