#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH --nodes 20
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --mem MaxMemPerNode
#SBATCH --partition medium
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/e%a.log
#SBATCH --error=errors/e%a.err
#SBATCH --array=0-39%20

echo "Starting at wall clock time:"
date
echo "Running CMT on $SLURM_CPUS_ON_NODE CPU cores"

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
python3 emb_modes.py 0 0 $SLURM_ARRAY_TASK_ID 
echo "Ending convergence study:"
date
