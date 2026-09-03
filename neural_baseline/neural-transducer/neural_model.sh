source /dss/dsshome1/03/ge87wod2/miniconda/etc/profile.d/conda.sh 
conda init
conda env create -n nt -f environment.yml 
conda activate nt

# Print some info
echo "Running on $(hostname)"
echo "Using Python from $(which python)"

# Run your Python script
bash example/sigmorphon2023-shared-tasks/task0-trm.sh
