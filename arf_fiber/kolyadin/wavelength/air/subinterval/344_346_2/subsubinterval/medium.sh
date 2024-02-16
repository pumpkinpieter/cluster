#!/usr/bin/bash
#SBATCH --job-name arfemb 
#SBATCH -N 40
#SBATCH -n 40
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
for i in 12 15 16 30 32 37 38 40 42 45 48 53 60 61 \
    63 68 69 76 78 80 81 84 87 89 90 91 101 105 107 \
    109 113 114 116 125 128 132 133 136 138 144 146 \
    147 148 151 157 161 163 166 168 169 173 176 183 \
    185 194 196 199 200 201 203 206 208 215 220 221 \
    225 226 227 238 240 242 246 249 255 273 276 278 \
    281 286 291 292 294 296 299 301 306 310 315 317 \
    318 321 322 326 328 329 332 334 336 339 343 345 \
    347 348 350 351 356 357 361 363 364 366 367 377 \
    378 380 384 391 394 398
    do
        module load ngsolve/myserial gcc-9.2.0 intel
        srun --unbuffered --nodes 1 --ntasks 1 \
            --output="logs/e_${i}_task_%s.out" \
            --error="errors/e_${i}_task_%s.err" \
            python3 emb_modes.py 0 6 ${i} &
done
wait
