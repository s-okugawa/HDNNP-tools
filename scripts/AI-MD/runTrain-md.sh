# main command
root=$PWD

for i in "1000K" "1200K"; do
    for j in $(seq 1 10); do
        dir=${root}/${i}/${j}
        cd ${dir}
        qsub run.csh
    done
done
#end

