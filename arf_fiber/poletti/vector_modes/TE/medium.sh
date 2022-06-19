#!/usr/bin/bash
#SBATCH --job-name TE
#SBATCH -N 36
#SBATCH -n 36
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/TE.log
#SBATCH --error=errors/TE.err

# Load needed modules.
module load ngsolve/serial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
for i in {0..17}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/ref0_p${i}.out" \
            --error="errors/ref0_p${i}.err" \
            python3 vector.py 0 ${i} &
done

for j in {0..11}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/ref1_p${j}.out" \
            --error="errors/ref1_p${j}.err" \
            python3 vector.py 1 ${j} &
done

for k in {0..5}
    do
        srun --exclusive --nodes 1 --ntasks 1 \
            --output="logs/ref2_p${k}.out" \
            --error="errors/ref2_p${k}.err" \
            python3 vector.py 2 ${k} &
done
wait
