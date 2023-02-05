#!/usr/bin/bash
#SBATCH --job-name getmode 
#SBATCH -N 4
#SBATCH -n 4
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium 
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/getmode.log
#SBATCH --error=errors/getmode.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
srun --unbuffered --nodes 1 --ntasks 1 python3 get_mode.py 0 3 0 &
srun --unbuffered --nodes 1 --ntasks 1 python3 get_mode.py 0 3 0.1 &
srun --unbuffered --nodes 1 --ntasks 1 python3 get_mode.py 0 3 0.05 &
srun --unbuffered --nodes 1 --ntasks 1 python3 get_mode.py 0 3 0.025
