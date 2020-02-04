# main command
root=$PWD

for bsx in "gs" "bs1" "bs2" "bs3" "bs4" "bs5" "bs6" "bs7" "bs8"; do
    qsub runPCstd.csh ${bsx}
done
#end