#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 25
#SBATCH -n 25
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long
#SBATCH --mem 0
#SBATCH --output=logs/log2.out
#SBATCH --error=errors/log2.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user piet2@pdx.edu

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

#rm logs/*task*
#rm errors/*task*

# Run the code.
echo "Starting convergence study: "
date
for i in {0..239}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/2e_${i}_task%s.out" \
            --error="errors/2e_${i}_task%s.err" \
            python3 driver240.py 0 4 ${i} 0.005 &
done
wait
