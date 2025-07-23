### Multiple Job Index
Use `-J` flag and `[]` to specify number of jobs in job array. The `%` (optional) sets how many concurrent running jobs
```sh
#!/bin/bash
#SBATCH --partition=normal        (specify queue)
#SBATCH --job-name=jobname        # base job name
#SBATCH --array=1-1000%3          # job array index: 1 to 1000, max 3 running at a time
#SBATCH --output=out/%A_%a.std_log.out
#SBATCH --error=out/%A_%a.error_log.err
```
`%A`: job ID, `%a`: array task index

