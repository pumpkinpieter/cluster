#!/usr/bin/bash
#SBATCH --job-name 3csgarf
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 24
#SBATCH --partition himem
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
for i in {16..17}
    do
        srun --exclusive --nodes 1 --ntasks 1 python3 vector.py 0 ${i} &
done

for j in {10..11}
    do
        srun --exclusive --nodes 1 --ntasks 1 python3 vector.py 1 ${j} &
done
wait
