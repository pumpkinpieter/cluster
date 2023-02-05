#!/usr/bin/bash
#SBATCH --job-name glass 
#SBATCH -N 12
#SBATCH -n 12
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long 
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/glass.out
#SBATCH --error=errors/glass.err
#SBATCH --mail-type ALL

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
for i in {0..11}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/maxh_0_p${i}_task%s.out" \
           --error="errors/maxh_0_p${i}_task%s.err" \
           python3 vector.py 1 ${i} 0.1 &
done

wait
