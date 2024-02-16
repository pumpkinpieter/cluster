#!/usr/bin/bash
#SBATCH --job-name arfemb 
<<<<<<< HEAD
#SBATCH -N 4
#SBATCH -n 4
=======
#SBATCH -N 11
#SBATCH -n 11
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
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
<<<<<<< HEAD
for i in 187 188 189 190 
=======
for i in {267..399}
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            --cpus-per-task 20 \
<<<<<<< HEAD
            python3 emb_modes.py 0 6 ${i} &
=======
            python3 emb_modes.py 0 7 ${i} &
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
done
wait
