#!/usr/bin/bash
#SBATCH --job-name bragconv
#SBATCH -N 13
#SBATCH -n 13
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --mail-type=ALL
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --output=logs/log.out
#SBATCH --error=errors/error.err

# Load needed modules.
module load ngsolve/myserial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
for i in {3..6}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref${i}_p0_task%s.out" \
           --error="errors/ref${i}_p0_task%s.err" \
           python3 driver.py ${i} 0 0 &
done

for j in {3..6}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref${j}_p1_task%s.out"\
           --error="errors/ref${j}_p1_task%s.err"\
           python3 driver.py ${j} 1 0 &
done

for k in {2..6}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref${k}_p2_task%s.out"\
           --error="errors/ref${k}_p2_task%s.err"\
           python3 driver.py ${k} 2 0 &
done
wait
