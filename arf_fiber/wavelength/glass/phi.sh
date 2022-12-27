#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 8
#SBATCH -n 8
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 40
#SBATCH --partition phi
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piet2@pdx.edu

# Load needed modules.
module load ngsolve/phi_serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
date
for i in {0..7}
    do
        module load ngsolve/phi_serial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            --cpus-per-task 40 \
            python3 emb_modes.py 0 4 ${i} &
done
wait
