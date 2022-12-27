#!/usr/bin/bash

#SBATCH --job-name arfemb 
#SBATCH -N 60
#SBATCH -n 60
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

ref=1
p=8
L=212
R=224
N=60
l=0.905
h=0.92

# Run the code.
echo "Starting convergence study: "
date

mkdir -p index_${L}_${R}/logs index_${L}_${R}/errors;

end="$((N-1))"

for i in $(seq 0 $end)
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="index_${L}_${R}/logs/e_${i}.out" \
            --error="index_${L}_${R}/errors/e_${i}.err" \
            python3 sub_modes.py $ref $p $i $L $R $N $l $h &
done
wait
