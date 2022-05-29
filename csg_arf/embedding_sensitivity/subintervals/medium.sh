#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 80
#SBATCH -n 80
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out

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

for i in {$L..$R}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/e_${i}.out" \
            --error="errors/e_${i}.err" \
            python3 sub_modes.py $ref $p ${i} $L $R $N $l $h &
done
wait
