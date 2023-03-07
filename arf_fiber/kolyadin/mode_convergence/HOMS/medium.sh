#!/usr/bin/bash
#SBATCH --job-name funarf 
#SBATCH -N 30
#SBATCH -n 30
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/funarf.out
#SBATCH --error=errors/funarf.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
for i in {0..14}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 vector.py 0 ${i} &
done

for j in {0..9}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref1_p${j}_task%s.out"\
           --error="errors/ref1_p${j}_task%s.err"\
           python3 vector.py 1 ${j} &
done

for k in {0..4}
    do
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref2_p${k}_task%s.out"\
           --error="errors/re2_p${k}_task%s.err"\
           python3 vector.py 2 ${k} &
done
wait
