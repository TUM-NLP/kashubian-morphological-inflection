#!/bin/bash
#SBATCH --partition=lrz-dgx-a100-80x8
#SBATCH --gres=gpu:1
#SBATCH --time=08:00:00
#SBATCH --output=%j.out

# Load Conda
# module load anaconda

# Activate your environment
conda init
conda activate nt

# Print some info
echo "Running on $(hostname)"
echo "Using Python from $(which python)"

# Run your Python script
bash example/sigmorphon2023-shared-tasks/task0-trm.sh
