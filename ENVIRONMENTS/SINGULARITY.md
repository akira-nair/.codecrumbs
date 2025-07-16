# Singularity

#### Convert docker image to singularity
```sh
module load singularity
singularity pull docker://<docker container on dockerhub>
```

#### Run script in container
```sh
singularity exec --bind $PWD:$PWD \
                ./environment.sif \
                python $PWD/my_script.py
```