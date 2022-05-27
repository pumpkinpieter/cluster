#!/usr/bin/bash
#SBATCH --job-name csgarf
#SBATCH -N 4
#SBATCH -n 4
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long 
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
#for i in {0..17}
#    do
#        srun --exclusive --nodes 1 --ntasks 1 python3 vector.py 0 ${i} &
#done

for j in {10..13}
    do
        srun --exclusive --nodes 1 --ntasks 1 python3 vector.py 1 ${j} &
done

#for k in {0..5}
#    do
#        srun --exclusive --nodes 1 --ntasks 1 python3 vector.py 2 ${k} &
#done
#wait
