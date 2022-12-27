#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 25
#SBATCH -n 25
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out
#SBATCH --array=0-1%1

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
t=$SLURM_ARRAY_TASK_ID
for i in {0..239}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
            python3 clad_emb.py 0 3 ${i} $t &
done
wait
