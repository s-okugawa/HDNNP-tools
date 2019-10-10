# main command
root=$PWD

for k in $(seq 20 20 100); do
    for i in "50" "100" "200" "300" "500"; do
        folder="d"${k}"n"${i}
        for j in $(seq 1 1 5); do
            dir=${root}/${folder}/${j}/predict-phonopy
            cd ${dir}
            rm std*
        done
    done
done
#end
