
#### Number of files
```sh
wc -l /path/to/dir
```

#### Search for keyboard among out files
```sh
grep ./*.out "keyword"
```
or get a list of files with keyword
```sh
grep ./*.out "keyword" -l
```

#### File sizes
```sh
du -h ./file.txt # for single file
du -h ./ # for all files in folder
du -sh ./ # for whole folder size
```

#### Tar Compress a folder
```
tar -czvf output.tar.gz /path/to/folder_or_file
```
