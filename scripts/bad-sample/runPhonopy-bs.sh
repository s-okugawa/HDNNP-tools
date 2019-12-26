# main command
root=$PWD

for bsx in "bs1" "bs2" "bs3" "bs4" "bs5" "bs6" "bs7" "bs8"; do
    folder=${bsx}"-d20n50"
    for j in $(seq 1 10); do
        dir=${root}/${folder}/${j}/predict-phonopy
        cd ${dir}
        python phonopyPrep.py --prefix Crystal --poscar POSCAR-unitcell --dim 2 2 2
        hdnnpy predict
        python phonopyRun.py --prefix Crystal --dim 2 2 2 --poscar POSCAR-unitcell --mesh 2 2 2
    done
done
#end