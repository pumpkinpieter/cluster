#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 50
#SBATCH -n 50
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
for i in {0..399}
    do
        module load gcc-9.2.0
        module load intel
        module load ngsolve/serial
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/task_%s_e_${i}.out" \
            --error="errors/task_%s_e_${i}.err" \
            python3 emb_modes.py 1 8 ${i} &
done
wait
