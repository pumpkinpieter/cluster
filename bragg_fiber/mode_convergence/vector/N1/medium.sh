#!/usr/bin/bash
#SBATCH --job-name bragconv
#SBATCH -N 3
#SBATCH -n 3
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
for i in {9..11}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 driver.py 0 ${i} 0 &
done
#
#for j in {0..6}
#    do
#        module load ngsolve/myserial gcc-9.2.0 intel
#        srun --unbuffered --nodes 1 --ntasks 1 \
#           --output="logs/ref1_p${j}_task%s.out"\
#           --error="errors/ref1_p${j}_task%s.err"\
#           python3 driver.py 1 ${j} 0 &
#done
#
#for k in {0..2}
#    do
#        module load ngsolve/myserial gcc-9.2.0 intel
#        srun --unbuffered --nodes 1 --ntasks 1 \
#           --output="logs/ref2_p${k}_task%s.out"\
#           --error="errors/ref2_p${k}_task%s.err"\
#           python3 driver.py 2 ${k} 0 &
#done
wait
