# Aliases

Some helpful aliases to copy into a `.bashrc` file. 

### LSF
```sh
alias lab="cd <path_to_lab_folder>"
alias myq="watch bjobs"
alias gpuq="watch bjobs -u all -q kimgpu"
alias grabcpu="bsub -q <normal_queue_name> -Is bash"
alias grabgpu="bsub -q <gpu_queue_name> -gpu 1 -Is bash"
alias ealias="vim ~/.bash_aliases"
```

### SLURM
```sh
alias lab="cd <path_to_lab_folder>"
alias myq="squeue -u <username>"
```

### LOCAL
```sh
hpc='ssh user@cluster_address'
hpcscp='function _scp2cluster() { scp "$1" user@cluster_address:"$2"; }; _scp2cluster'
```