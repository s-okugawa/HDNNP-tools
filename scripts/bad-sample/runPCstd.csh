#!/bin/csh
#$ -cwd
#$ -V -S /bin/bash
#$ -N PC-standardization
#$ -o stdout
#$ -e stderr
#$ -q all.q
#$ -pe smp 24

PIPENV_PIPFILE=$HOME/HDNNP/Pipfile
pipenv run python stdPC123-batch.py $1