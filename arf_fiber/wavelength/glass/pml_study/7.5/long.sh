#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 14
#SBATCH -n 14
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long
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
p=4
for i in {0..199}
    do
        module load ngsolve/serial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_p${p}_task_%s.out" \
            --error="errors/e_${i}_p${p}_task_%s.err" \
            --cpus-per-task 20 \
            python3 emb_modes.py 0 $p ${i} &
done
wait
