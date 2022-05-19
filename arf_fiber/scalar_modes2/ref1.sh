#!/usr/bin/bash
#SBATCH --job-name arfscr1
#SBATCH --nodes 4
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --mem MaxMemPerNode
#SBATCH --partition medium 
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/ref1_%a.log
#SBATCH --error=errors/ref1_%a.err
#SBATCH --array=1-4%2

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
python3 scalar_convergence.py 1 $SLURM_ARRAY_TASK_ID
echo "Ending convergence study:"
date
