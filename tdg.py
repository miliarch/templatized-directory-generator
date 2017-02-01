#!/usr/bin/env python3
''' Templatized Directory Generator
Read defined templates from JSON configuration file, generate the
defined directory/file structure on disk.


Author: Marcus Bowman
File name: tdg.py
Version: 0.2
Date created: 01/29/2017
Date last modified: 01/29/2017
Python Version: 3.5.2
OS Support: Linux, OS X
License: MIT
'''
import json
import sys
from argparse import ArgumentParser
from pathlib import Path, PurePath

EXEC_DIR = Path.cwd().resolve()
BASE_DIR = Path(__file__).parents[0]
TEMPLATES_FILENAME = PurePath(BASE_DIR, 'templates.json')

def exception_exit(help_str):
    """ Exit on fatal exception, printing help string """
    print(help_str)
    sys.exit(2)


def import_config_json(filename):
    """ Import data from JSON configuration file, return dict """
    try:
        with open(filename, encoding='utf-8') as file:
            config = json.loads(file.read())
    except FileNotFoundError as err:
        exception_exit('JSON config file not found:\n{}'.format(err))
    except json.decoder.JSONDecodeError:
        exception_exit('File contents not JSON format:\n{}'.format(filename))
        

    return config


def parse_args(args):
    """ Take from argparse, match to defined template in templates.json,
    return relevant template as dict
    """

    # Found this bit posted by unutbu here: http://stackoverflow.com/a/4042861
    class Parser(ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: {0}\n'.format(message))
            self.print_help()
            sys.exit(2)

    parser = Parser(
        description='Create DIRs from templates defined in templates.json')
    parser.add_argument('template',
        help='Template to use for DIR structure')
    parser.add_argument('dir_name', 
        help='Name for parent directory in base DIR defined by template')
    args = parser.parse_args()

    return args


def select_template(template_name):
    templates = import_config_json(str(TEMPLATES_FILENAME))

    try:
        template = templates[template_name]
    except KeyError as err:
        exception_exit('Specified template not defined in "{0}":\n{1}'.format(
            TEMPLATES_FILENAME,
            err))

    return template


def path_add_str(full_path):
    return '+ {}'.format(full_path)


def update_paths(dir_name, template):
    """ Update all paths in template dict to absolute values """
    try:
        template['base_dir'] = [PurePath(template['base_dir'], dir_name)]
    except KeyError:
        template['base_dir'] = [PurePath(EXEC_DIR, dir_name)]

    for i,sub_dir in enumerate(template['sub_dirs']):
        template['sub_dirs'][i] = PurePath(template['base_dir'][0], sub_dir)

    for i,file in enumerate(template['files']):
        template['files'][i] = PurePath(template['base_dir'][0], file)

    return template


def write_paths(paths, is_file=False):
    for p in paths:
        Path(p).touch() if is_file else Path(p).mkdir()
        print(path_add_str(p))


def main(args):
    args = parse_args(args)
    template = update_paths(args.dir_name, select_template(args.template))

    # Get to business
    write_paths(template['base_dir'], is_file=False)
    write_paths(template['sub_dirs'], is_file=False)
    write_paths(template['files'], is_file=True)


if __name__ == '__main__':
    main(sys.argv)