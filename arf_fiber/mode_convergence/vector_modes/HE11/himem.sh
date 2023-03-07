#!/usr/bin/bash
#SBATCH --job-name arf
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 24
#SBATCH --partition himem
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/arf_convergence.log
#SBATCH --error=errors/arf_convergence.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {18..19}
    do
        srun --unbuffered --nodes 1 --ntasks 1 python3 vector.py 0 ${i} &
done

for j in {12..13}
    do
        srun --unbuffered --nodes 1 --ntasks 1 python3 vector.py 1 ${j} &
done
wait
