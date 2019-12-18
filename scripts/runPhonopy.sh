# main command
root=$PWD

for k in $(seq 20 20 100); do
    for i in "50" "100" "200" "300" "500"; do
        folder="d"${k}"n"${i}
        for j in $(seq 6 1 10); do
            dir=${root}/${folder}/${j}/predict-phonopy
            cd ${dir}
            python phonopyPrep.py --prefix Crystal --poscar POSCAR-unitcell --dim 2 2 2
            hdnnpy predict
            python phonopyRun.py --prefix Crystal --dim 2 2 2 --poscar POSCAR-unitcell --mesh 2 2 2
        done
    done
done
#end
