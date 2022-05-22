#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH --nodes 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 24
#SBATCH --partition himem
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/himem_e.log
#SBATCH --error=errors/himem_e.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {0..39}
    do
        srun --exclusive --nodes 1 --ntasks 1 python3 emb_modes.py 0 12 ${i} &
done
wait
