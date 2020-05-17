# main command
root=$PWD

for k in $(seq $1 $2); do
    qdel ${k}
done
