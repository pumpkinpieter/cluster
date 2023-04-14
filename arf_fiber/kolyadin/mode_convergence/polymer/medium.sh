#!/usr/bin/bash
#SBATCH --job-name funarf 
#SBATCH -N 22
#SBATCH -n 22
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type=ALL
#SBATCH --output=logs/funarf.out
#SBATCH --error=errors/funarf.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

rm logs/*ref*
rm errors/*ref*

# Run the code.
echo "Starting convergence study: "
for i in {0..11}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 driver.py 0 ${i} &
done

for j in {0..9}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref1_p${j}_task%s.out"\
           --error="errors/ref1_p${j}_task%s.err"\
           python3 driver.py 1 ${j} &
done
wait
