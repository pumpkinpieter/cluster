#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH --cpus-per-task 20
#SBATCH --partition himem
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
i=143
srun --output="logs/e_${i}_task_%s.out" \
    --error="errors/e_${i}_task_%s.err" \
    python3 emb_modes.py 0 6 ${i}
