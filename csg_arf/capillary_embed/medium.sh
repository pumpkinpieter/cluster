#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 60
#SBATCH -n 60
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/e%a.log
#SBATCH --error=errors/e%a.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {0..239}
    do
        srun --exclusive --nodes 1 --ntasks 1 python3 emb_modes.py 1 8 ${i} &
done
wait
