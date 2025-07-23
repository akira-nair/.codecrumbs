# Aliases

Aliases are shortcuts for shell commands. Sometimes it's tough to memorize the longer ones,
so I like to make aliases for the ones I use often. To set up aliases, first determine the 
type of shell you are using by running `echo $0`. Usually, this is either a `zsh` or `bash`.
Then identify the rc file, e.g. `~/.zshrc` or `~/.bashrc`. You can edit this file using one
of the built in text editors, such as vim or nano, e.g. `vim ~/.zshrc`. Copy and paste some of
these aliases! I usually have ones that cd into a folder I use a lot, something to live monitor
my jobs, start interactive sessions, and copy files (scp) onto the cluster. 
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