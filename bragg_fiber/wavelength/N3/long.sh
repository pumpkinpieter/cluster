#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 19
#SBATCH -n 19
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piet2@pdx.edu

# Load needed modules.
module load ngsolve/myserial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in 7 8 41 43 47 52 57 58 64 76 79 89 98 100 \
    101 103 110 115 138 142 148 152 155 159 163 167 \
    173 175 177 180 182 184 186
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            python3 driver.py 0 5 ${i} &
done
wait
