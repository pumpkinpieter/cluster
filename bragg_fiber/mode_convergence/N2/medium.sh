#!/usr/bin/bash
#SBATCH --job-name bragconv
<<<<<<< HEAD
#SBATCH -N 12
#SBATCH -n 12
=======
#SBATCH -N 19
#SBATCH -n 19
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
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
<<<<<<< HEAD
for i in {0..6}
=======
for i in {0..7}
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${i}_task%s.out" \
           --error="errors/ref0_p${i}_task%s.err" \
           python3 driver.py 0 ${i} 0 &
done

<<<<<<< HEAD
for j in {0..4}
=======
for j in {0..5}
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref1_p${j}_task%s.out"\
           --error="errors/ref1_p${j}_task%s.err"\
           python3 driver.py 1 ${j} 0 &
done
<<<<<<< HEAD
=======

for k in {0..3}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref2_p${k}_task%s.out"\
           --error="errors/re2_p${k}_task%s.err"\
           python3 driver.py 2 ${k} 0 &
done
>>>>>>> 4fac300c54dc7d0417a5fd711f9fde1c8c2a4aa5
wait
