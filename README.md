# Templatized Directory Generator

Generate new directory structure from JSON template, using arguments passed to command for unique naming

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

## Example JSON (./templates.json)
```
{
    "template": {
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
    }
}
```

## Example Run
```
miliarch@localhost:~$ tdg template my-dir-name
+ /home/miliarch/my-dir-name/test1/
+ /home/miliarch/my-dir-name/test1/level2/
+ /home/miliarch/my-dir-name/test2/
+ /home/miliarch/my-dir-name/test3/
+ /home/miliarch/my-dir-name/test4/
+ /home/miliarch/my-dir-name/test1/level2_file.txt
+ /home/miliarch/my-dir-name/test1/level2/level3_file.txt
+ /home/miliarch/my-dir-name/test3/level2_file.txt
+ /home/miliarch/my-dir-name/level1_file.txt
```