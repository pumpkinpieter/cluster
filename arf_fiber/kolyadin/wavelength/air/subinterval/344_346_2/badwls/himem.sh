#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 24
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
echo "Starting convergence study: "
date
#
#for i in 7 8
#    do
#        srun --unbuffered --nodes 1 --ntasks 1 \
#            --output="logs/e_${i}_task_%s.out" \
#            --error="errors/e_${i}_task_%s.err" \
#            --cpus-per-task 24 \
#            python3 emb_modes.py 0 ${i} 64 &
#done
#
for j in 9 10
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            --cpus-per-task 24 \
            python3 emb_modes.py 0 ${j} 108 &
done

for k in 9 10
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            --cpus-per-task 24 \
            python3 emb_modes.py 0 ${k} 347 &
done
wait
