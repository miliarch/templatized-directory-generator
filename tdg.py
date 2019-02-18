#!/usr/bin/env python3
""" Templatized Directory Generator

Reads defined templates from JSON configuration file, generates the defined
directory/file structure of the user's specified template on the filesystem.
"""

__author__ = "Marcus Bowman"
__email__ = "miliarch.mb@gmail.com"
__license__ = "MIT"
__version__ = "0.3"
__status__ = "Development"

import json
import sys
from argparse import ArgumentParser
from pathlib import Path, PurePath

EXEC_DIR = Path.cwd().resolve()
BASE_DIR = Path(__file__).resolve().parents[0]
TEMPLATES_FILENAME = PurePath(BASE_DIR, 'templates.json')


def exception_exit(help_str):
    """Exit on fatal exception, printing help string"""
    print(help_str)
    sys.exit(2)


def import_config_json(filename):
    """Import data from JSON configuration file, return dict"""
    try:
        with open(filename, encoding='utf-8') as file:
            config = json.loads(file.read())
    except FileNotFoundError as err:
        help_str = 'JSON config file not found:\n{}'.format(err)
        exception_exit(help_str)
    except json.decoder.JSONDecodeError as err:
        help_str = 'JSON decode error:\n{}\n{}'.format(err, filename)
        exception_exit(help_str)

    return config


def parse_args(args):
    """ Parse and return passed arguments """

    # Found this bit posted by unutbu here: http://stackoverflow.com/a/4042861
    class Parser(ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: {0}\n'.format(message))
            self.print_help()
            sys.exit(2)

    description = 'Create directory structure based on templates '
    description += 'defined in templates.json'
    parser = Parser(description=description)

    help_str = 'Template to use for directory structure'
    parser.add_argument('template', help=help_str)

    help_str = 'Name for new directory'
    parser.add_argument('dir_name', help=help_str)

    args = parser.parse_args()

    return args


def select_template(template_name):
    """ Import templates.json as dict, return specified template_name if
    it exists in the dict, exit if it does not exist
    """
    templates = import_config_json(str(TEMPLATES_FILENAME))

    try:
        template = templates[template_name]
    except KeyError as err:
        help_str = 'Template {0} not defined in:\n{1}'.format(
            err,
            TEMPLATES_FILENAME)
        exception_exit(help_str)

    return template


def path_add_str(path_):
    """ Format path_ for console printing """
    return '+ {}'.format(path_)


def update_paths(dir_name, template):
    """ Update all paths in template dict to absolute values """
    try:
        template['base_dir'] = [PurePath(template['base_dir'], dir_name)]
    except KeyError:
        template['base_dir'] = [PurePath(EXEC_DIR, dir_name)]

    for i, sub_dir in enumerate(template['sub_dirs']):
        template['sub_dirs'][i] = PurePath(template['base_dir'][0], sub_dir)

    for i, file in enumerate(template['files']):
        template['files'][i] = PurePath(template['base_dir'][0], file)

    return template


def write_paths(paths, is_file):
    """ Create directories or files in paths list, print path_add_str """
    for p in paths:
        Path(p).touch() if is_file else Path(p).mkdir()
        print(path_add_str(p))


def main(args):
    # Set the pins up
    args = parse_args(args)
    template = update_paths(args.dir_name, select_template(args.template))

    # Knock them down
    write_paths(template['base_dir'], is_file=False)
    write_paths(template['sub_dirs'], is_file=False)
    write_paths(template['files'], is_file=True)


if __name__ == '__main__':
    main(sys.argv)
