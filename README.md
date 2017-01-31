# Templatized Directory Generator

Read defined templates from JSON configuration file, generate the
defined directory/file structure on disk.

## Usage
```
usage: tdg [-h] template dir_name

Create DIRs from templates defined in templates.json

positional arguments:
  template    Template to use for DIR structure
  dir_name    Name for parent directory in base DIR defined by template

optional arguments:
  -h, --help  show this help message and exit
```

## Creating Templates
Simply move or copy templates.json.example to templates.json in the program directory, and modify as necessary. Paths are built using string concatenation, so only base_dir should an absolute path. If no path is specified as base_dir in a template definition, dir_name and all sub_dirs/files will be created in the current directory.

## Example JSON (./templates.json)
```
{
    "template1": {
        "sub_dirs": [
            "test1/",
            "test1/level2/",
            "test2/",
            "test3/",
            "test4/"
        ],
        "files": [
            "test1/level2_file.txt",
            "test1/level2/level3_file.txt",
            "test3/level2_file.txt",
            "level1_file.txt"
        ]
    },
    "template2": {
        "sub_dirs": ["test1/"],
        "files": ["file.txt", "test1/file.txt"]
    }
}
```

## Example Run
```
miliarch@localhost:~$ tdg template1 my-dir-name1
+ /home/miliarch/my-dir-name1/test1/
+ /home/miliarch/my-dir-name1/test1/level2/
+ /home/miliarch/my-dir-name1/test2/
+ /home/miliarch/my-dir-name1/test3/
+ /home/miliarch/my-dir-name1/test4/
+ /home/miliarch/my-dir-name1/test1/level2_file.txt
+ /home/miliarch/my-dir-name1/test1/level2/level3_file.txt
+ /home/miliarch/my-dir-name1/test3/level2_file.txt
+ /home/miliarch/my-dir-name1/level1_file.txt

PS C:\> python tdg.py template2 my-dir-name2
+ C:\/my-dir-name2/test1/
+ C:\/my-dir-name2/file.txt
+ C:\/my-dir-name2/test1/file.txt
```