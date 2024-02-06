#!/usr/bin/bash
#SBATCH --job-name funarf 
#SBATCH -N 18
#SBATCH -n 18
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition long 
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
for i in {0..7}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 emb_modes.py 0 ${i} 195 &
done

for j in {0..5}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref1_p${j}_task%s.out"\
           --error="errors/ref1_p${j}_task%s.err"\
           python3 emb_modes.py 1 ${j} 195 &
done

for k in {0..3}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref2_p${k}_task%s.out"\
           --error="errors/re2_p${k}_task%s.err"\
           python3 emb_modes.py 2 ${k} 195 &
done
wait
