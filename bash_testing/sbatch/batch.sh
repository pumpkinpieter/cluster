#!/usr/bin/bash

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date

ref=$1
p=$2
alpha=$3

for i in {0..199}
    do
        module load ngsolve/serial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_p${p}_task_%s.out" \
            --error="errors/e_${i}_p${p}_task_%s.err" \
            --cpus-per-task 20 \
            python3 driver.py $ref $p $alpha ${i} &
done
wait
