#!/usr/bin/bash
#SBATCH --job-name funarf 
#SBATCH -N 2
#SBATCH -n 2
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition himem 
#SBATCH --mem 0
#SBATCH --mail-user piet2@pdx.edu
#SBATCH --mail-type=ALL
#SBATCH --output=logs/funarf.out
#SBATCH --error=errors/funarf.err

# Load needed modules.
module load ngsolve/myserial
module load gcc-9.2.0
module load intel

# Run the code.
echo "Starting convergence study: "
for i in {7..12}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 emb_modes.py 0 ${i} 192 &
done
#
#for j in {6..9}
#    do
#        module load ngsolve/myserial gcc-9.2.0 intel
#        srun --unbuffered --nodes 1 --ntasks 1 \
#           --output="logs/ref1_p${j}_task%s.out"\
#           --error="errors/ref1_p${j}_task%s.err"\
#           python3 emb_modes.py 1 ${j} 195 &
#done
wait
