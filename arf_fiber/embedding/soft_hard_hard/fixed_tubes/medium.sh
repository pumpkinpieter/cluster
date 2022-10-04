#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 6
#SBATCH -n 6
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
        module load ngsolve/serial intel gcc-9.2.0
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            python3 emb_modes.py 0 3 ${i} &
done
wait
