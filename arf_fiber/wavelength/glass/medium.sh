#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 21
#SBATCH -n 21
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piet2@pdx.edu

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in 2 4 5 6 7 9 10 11 13 14 17 18 19 20 \
    21 22 24 25 26 30 31 32 33 34 36 37 40 43 \
    51 53 56 58 59 60 61 62 64 66 67 68 69
do
    module load ngsolve/serial gcc-9.2.0 intel
    srun --unbuffered --nodes 1 --ntasks 1 \
        --output="logs/e_${i}_task_%s.out" \
        --error="errors/e_${i}_task_%s.err" \
        python3 emb_modes.py 0 4 ${i} &
done
wait
