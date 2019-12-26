# main command
root=$PWD

for bsx in "bs1" "bs2" "bs3" "bs4" "bs5" "bs6" "bs7" "bs8"; do
    folder=${bsx}"-d20n50"
    for j in $(seq 1 10); do
        dir=${root}/${folder}/${j}
        cd ${dir}
        qsub run.csh
    done
done
#end
