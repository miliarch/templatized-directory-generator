# Templatized Directory Generator

Generate new directory structure from JSON template, using arguments passed to command for unique naming

## Example JSON
```
{
    'template_name': {
        'base_dir': '/foo/bar/',
        'sub_dirs': ['dir1/', 'dir2/', 'dir2/another_level/'],
        'files': ['dir_file.txt', 'dir1/subdir_file.txt']
    }
}
```

## Example CLI args
```
tdg.py [-i|--id] <id> [-s|--subject] "<subject>"
```

## Output
```
/foo/bar/<id>_<subject-to-str>/
├──dir1/
│  └──subdir_file.txt
├──dir2/
│  └──another_level/
└──dir_file.txt
```