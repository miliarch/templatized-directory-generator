# Templatized Directory Generator

Reads defined templates from JSON configuration file, generates the defined directory/file structure of the user's specified template on the filesystem.

## Goals and Use Cases
It's common to use different and specific folder/file structures for different types of work. The goal of this tool is to allow the user to define templates to simplify directory structure build-out when starting new projects. Current plans are centered around creation of the directories and files, and do not extend to adding content to any files created.

### Use Case: Investigative work
I've spent a great deal of my professional life in technical support roles, and I find that most case work in a given area fits into a few basic categories, each with different evidence documentation requirements. Creating templates for common case types helps me save time during the investigative process. Not only does directory contents serve as a checklist of important evidence to gather, but it removes the need to think about data organization during the discovery and documentation process.

### Use Case: Programming
Benefits in programming workflows should be immediately obvious. Different languages and technologies suggest or require certain project directory structures. People build their own preferences and requirements during the course of developing their projects. Remembering and reconciling these things incurs overhead. Using templates when projects are started, and updating definitions when requirements change for future projects, saves effort in the long term.

Examples of use cases in programming:

* Set up a basic module template for your Python projects (see: [Structuring Your Project](https://docs.python-guide.org/writing/structure/))
* Create .gitignore and .gitattributes files in the root of your projects
* Create a standard configuration file if your programs generally include them
* Create standard sub directories, such as tests, doc, src, help, etc.

## Usage
```
usage: tdg [-h] template dir_name

Create DIRs from templates defined in templates.json

positional arguments:
  template    Template to use for creating DIR structure
  dir_name    Name for parent directory in template defined base DIR

optional arguments:
  -h, --help  show this help message and exit
```

## Creating Templates
Simply move or copy templates.json.example to templates.json in the program directory, and modify as necessary. Only base_dir should be an absolute path, all other paths are relative.

If no path is specified as base_dir in a template definition, dir_name and all sub_dirs/files will be created in the user's current working directory.

## Example
This is a simple example of the "Investigative work" use case mentioned above.

### templates.json
```
{
    "support_case": {
        "base_dir": "/cases",
        "sub_dirs": [
            "screenshots",
            "logs"
        ],
        "files": [
            "problem.txt",
            "scratch_notes.txt",
            "timeline.txt",
            "solution.txt"
        ]
    }
}
```

### Program run
```
$ ./tdg.py support_case 12345_description
+ /cases/12345_description
+ /cases/12345_description/screenshots
+ /cases/12345_description/logs
+ /cases/12345_description/problem.txt
+ /cases/12345_description/scratch_notes.txt
+ /cases/12345_description/timeline.txt
+ /cases/12345_description/solution.txt
```

### Filesystem representation
```
$ ls -lnGXR /cases/12345_description
/cases/12345_description:
total 0
drwxrwxrwx 1 1000 512 Feb 17 14:48 logs
drwxrwxrwx 1 1000 512 Feb 17 14:48 screenshots
-rw-rw-rw- 1 1000   0 Feb 17 14:48 problem.txt
-rw-rw-rw- 1 1000   0 Feb 17 14:48 scratch_notes.txt
-rw-rw-rw- 1 1000   0 Feb 17 14:48 solution.txt
-rw-rw-rw- 1 1000   0 Feb 17 14:48 timeline.txt

/cases/12345_description/logs:
total 0

/cases/12345_description/screenshots:
total 0
```
