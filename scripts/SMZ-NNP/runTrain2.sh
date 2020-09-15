# main command
root=$PWD

folder="training_1element-smzsf/"
for j in $(seq 11 20); do
    dir=${root}/${folder}/${j}
    cd ${dir}
    qsub run.csh
done
#end
