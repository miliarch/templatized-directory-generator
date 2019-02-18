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
usage: tdg.py [-h] template dir_name

Create directory structure based on templates defined in templates.json

positional arguments:
  template    Template to use for directory structure
  dir_name    Name for new directory

optional arguments:
  -h, --help  show this help message and exit
```

## Defining Templates
Templates can be defined by crafting JSON using the fields below within objects named for each template in the `templates.json` configuration file:

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| base_dir | String | Absolute file system path of the parent directory. If no base_dir is specified for a template, the user's current working directory will be used. | `"base_dir": "/home/user/projects"` |
| sub_dirs | Array of Strings | List of relative sub-directory path strings to be created under base_dir/dir_name/ | `"sub_dirs": ["subdir1", "subdir1/subdir2"]` |
| files | Array of Strings | List of relative file paths strings to be created under base_dir/dir_name/ | `"files": ["file.txt", "subdir1/file.txt"]` |

A full example template can be found below.

### Special values

The following values can be used in template definition to reflect arguments passed by the user at the command line:

| Value | Meaning | Example |
| --- | --- | --- |
| !dir_name! | Use the dir_name passed in arguments at run time as the file/directory name | `"sub_dirs": ["!dir_name!", "tests"], "files": ["!dir_name!.py", "!dir_name!/__init__.py", "README.md", "LICENSE"]`|

## Example
This is a simple example of templates definition and program use, covering the use case mentioned above.

### templates.json
```
{
    "python_basic": {
        "base_dir": "/projects",
        "sub_dirs": [
            "!dir_name!/",
            "docs",
            "tests"
        ],
        "files": [
            "!dir_name!/__init__.py",
            "run.py",
            "README.md",
            "LICENSE",
            ".gitignore",
            ".gitattributes"
        ]
    },
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

### Running the program
```
$ ./tdg.py python_basic new_proj1
+ /projects/new_proj1
+ /projects/new_proj1/new_proj1
+ /projects/new_proj1/docs
+ /projects/new_proj1/tests
+ /projects/new_proj1/new_proj1/__init__.py
+ /projects/new_proj1/run.py
+ /projects/new_proj1/README.md
+ /projects/new_proj1/LICENSE
+ /projects/new_proj1/.gitignore
+ /projects/new_proj1/.gitattributes

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
$ tree --dirsfirst /projects/new_proj1
/projects/new_proj1
├── docs
├── new_proj1
│   └── __init__.py
├── tests
├── LICENSE
├── README.md
└── run.py

$ tree --dirsfirst /cases/12345_description
/cases/12345_description
├── logs
├── screenshots
├── problem.txt
├── scratch_notes.txt
├── solution.txt
└── timeline.txt
```
