#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date

ref=1
p=8
L=0
R=1
N=1
l=0
h=1

#SBATCH -N $N
#SBATCH -n $N
#SBATCH --output=inverval_${L}_${R}/logs/log.out
#SBATCH --error=inverval_${L}_${R}/errors/log.out

for i in {$L..$R}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="inverval_${L}_${R}/logs/e_${i}.out" \
            --error="inverval_${L}_${R}/errors/e_${i}.err" \
            python3 sub_modes.py $ref $p ${i} $L $R $N $l $h &
done
wait
