#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 49
#SBATCH -n 49
#SBATCH --tasks-per-node 1
#SBATCH --cpus-per-task 20
#SBATCH --partition medium
#SBATCH --mem 0
#SBATCH --output=logs/log.out
#SBATCH --error=errors/log.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piet2@pdx.edu

# Load needed modules.
module load ngsolve/myserial
module load gcc-9.2.0
module load intel

# rm logs/*task*
# rm errors/*task*

# Run the code.
echo "Starting convergence study: "
date
for i in 185 186 189 190 202 204 211 217 220 221 223 233 239 243 \
    244 246 247 248 249 252 258 260 262 264 268 270 276 278 279 \
    283 289 291 294 296 297 300 304 306 307 316 320 328 331 335 \
    336 358 360 361 364 365 369 371 372 373 375 376 378 379 381 \
    382 383 389 390 393 394 395 396 398

    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            python3 emb_modes.py 0 6 ${i} &
done
wait
