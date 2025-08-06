#!/usr/bin/bash
#SBATCH --job-name bragconv
#SBATCH -N 21
#SBATCH -n 21
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/error.err

# Load needed modules.
module load ngsolve/myserial
module load gcc-9.2.0
module load intel

if [ ! -d "logs" ]; then
      echo "making log directory."
      mkdir logs
  fi

if [ ! -d "errors" ]; then
      echo "making error directory."
      mkdir errors
  fi

p=9
alpha=10

# Run the code.
echo "Starting convergence study: "
for i in {0..20}
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
           --output="logs/ref0_p${p}_T${i}_task%s.out" \
           --error="errors/ref0_p${p}_T${i}_task%s.err" \
           python3 driver.py 0 $p $i $alpha &
done
wait
