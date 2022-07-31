#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 60
#SBATCH -n 60
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
for i in {0..239}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/e_${i}.out" \
            --error="errors/e_${i}.err" \
            python3 emb_modes.py 0 5 ${i} &
done
wait
