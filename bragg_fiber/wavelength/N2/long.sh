#!/usr/bin/bash
#SBATCH --job-name bragg
#SBATCH -N 28
#SBATCH -n 28
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long
#SBATCH --mem 0 
#SBATCH --output=logs/log.out
#SBATCH --error=errors/errors.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piet2@pdx.edu

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Clear log and error folders of old runs
rm logs/*wl*
rm errors/*wl*

# Run the code.
echo "Starting convergence study: "
date
for i in {0..300}
    do
        module load ngsolve/serial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/wl_${i}_task_%s.out" \
            --error="errors/wl_${i}_task_%s.err" \
            python3 driver.py 0 7 ${i} &
done
wait
