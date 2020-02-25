# main command
root=$PWD

for i in "p10" "p15" "p20"; do
    folder="d20n50-"${i}
    for j in $(seq 1 10); do
        dir=${root}/${folder}/${j}
        cd ${dir}
        qsub run.csh
    done
done
#end
