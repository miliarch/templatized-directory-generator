#!/usr/bin/env python3
''' Templatized Directory Generator


'''
import json
import os

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
        exception_exit('File contents JSON format:\n{}'.format(filename))
        

    return config

base_dir = os.path.abspath(os.path.dirname(__file__))
templates_filename = '{0}/templates.json'.format(base_dir)
templates = import_config_json(templates_filename)

print(templates)