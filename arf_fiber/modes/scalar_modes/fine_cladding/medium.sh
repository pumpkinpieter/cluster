#!/usr/bin/bash
#SBATCH --job-name csgarf
#SBATCH -N 42
#SBATCH -n 42
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/csg_arf_convergence.log
#SBATCH --error=errors/csg_arf_convergence.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {0..24}
    do
        srun --unbuffered --nodes 1 --ntasks 1 python3 scalar_convergence.py 0 ${i} &
done

for j in {0..16}
    do
        srun --unbuffered --nodes 1 --ntasks 1 python3 scalar_convergence.py 1 ${j} &
done
wait
