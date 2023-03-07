#!/usr/bin/bash
#SBATCH --job-name funarf 
#SBATCH -N 14
#SBATCH -n 14
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type ALL
#SBATCH --output=logs/funarf.out
#SBATCH --error=errors/funarf.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
p=6
echo "Starting convergence study: "
for i in {0..36}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${p}_alpha${i}_task%s.out" \
           --error="errors/ref0_p${p}_alpha${i}_task%s.err" \
           python3 vector.py 0 $p ${i} &
done
wait
