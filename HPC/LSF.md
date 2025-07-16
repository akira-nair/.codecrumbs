## Batch Script

### Basic Script
```sh
#!/bin/bash
#BSUB -q normal (or specify queue)
#BSUB -J jobname
#BSUB -o out/%J.std_log.out
#BSUB -e out/%J.error_log.err
```

### Multiple Job Index
Use `-J` flag and `[]` to specify number of jobs in job array. The `%` (optional) sets how many concurrent running jobs
```sh
#!/bin/bash
#BSUB -q normal (or specify queue)
#BSUB -J jobname[1-1000]%3
#BSUB -o out/%I.std_log.out
#BSUB -e out/%I.error_log.err
```
`%I` will make sure the out and err files will contain job index.

### GPU Script
```sh
#!/bin/bash
#BSUB -q kimgpu
#BSUB -m kimgroupgpu01 (for A100 or use ..gpu02 for H100)
#BSUB -gpu "num=2"
#BSUB -J gpujob
#BSUB -o out/gpu_job.%J.out
module load CUDA # or specify version e.g. CUDA/11.3
export CUDA_VISIBLE_DEVICES=0,1

python myscript.py
```