# main command
root=$PWD

for i in "1750smpl" "3500smpl"; do
    folder="SMZ-200901/"${i}
    for j in $(seq 1 10); do
        dir=${root}/${folder}/training_2element/${j}/poscar_elm2
        cd ${dir}
        python phono3py_shimizuNNP.py run > out.txt
    done
done