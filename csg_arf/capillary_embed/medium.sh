#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 5
#SBATCH -n 5
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=/log.out

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {201..205}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/e_${i}.out" --error="errors/e_${i}.err" \
            python3 emb_modes.py 1 8 ${i} 0 1 &
done
wait
