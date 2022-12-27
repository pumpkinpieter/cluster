#!/usr/bin/bash
#SBATCH --job-name arffillrange 
#SBATCH -N 50
#SBATCH -n 50
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {0..200}
    do
        module load ngsolve/serial
        module load intel
        module load gcc-9.2.0
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/delta_${i}_task%s.out" \
            --error="errors/delta_${i}_task%s.err" \
            python3 vector.py 0 12 ${i} &
done
wait
