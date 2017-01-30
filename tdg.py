#!/usr/bin/env python3
''' Templatized Directory Generator


'''
import argparse
import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_FILENAME = '{0}/templates.json'.format(BASE_DIR)

def exception_exit(help_str):
    """ Exit on fatal exception, printing help string """
    print(help_str)
    exit(2)


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
    class Parser(argparse.ArgumentParser):
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
    templates = import_config_json(TEMPLATES_FILENAME)

    try:
        template = templates[template_name]
    except KeyError as err:
        exception_exit('Specified template not defined in "{0}":\n{1}'.format(
            TEMPLATES_FILENAME,
            err))

    return template


def set_parent_dir():
    pass


def main(args):
    args = parse_args(args)
    template = select_template(args.template)

    dir_name = '{0}/'.format(args.dir_name)
    try:
        template['base_dir'] += dir_name
    except KeyError:
        template['base_dir'] = dir_name

    print(template)

if __name__ == '__main__':
    main(sys.argv)