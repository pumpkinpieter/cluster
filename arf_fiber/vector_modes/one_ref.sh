#!/usr/bin/bash
#SBATCH --job-name arfvecref1
#SBATCH --nodes 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 24
#SBATCH --mem MaxMemPerNode
#SBATCH --partition himem
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/ref1_p%a.log
#SBATCH --error=errors/ref1_p%a.err
#SBATCH --array=0-19%2

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
python3 vector_convergence.py 1 $SLURM_ARRAY_TASK_ID
echo "Ending convergence study:"
date
