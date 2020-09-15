# main command
root=$PWD

for i in "1750smpl" "3500smpl"; do
    for j in $(seq 1 10); do
        dir=${root}/${i}/training_2element/${j}
        cd ${dir}
        qsub run.csh
    done
done
#end