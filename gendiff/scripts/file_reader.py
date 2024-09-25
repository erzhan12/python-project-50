import json
import os

import yaml


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]


def parse(file_name, file_format):
    match file_format:
        case 'json':
            return json.load(open(file_name, 'r'))
        case 'yaml':
            return yaml.load(open(file_name, 'r'), yaml.FullLoader)


def get_absolute_path(file_name):
    if os.path.isabs(file_name):
        return file_name
    return os.path.abspath(os.path.join(os.getcwd(), file_name))


def get_format_name(extension):
    match extension:
        case '.json':
            return 'json'
        case '.yaml' | '.yml':
            return 'yaml'


def read_file(file_name):
    absolute_path = get_absolute_path(file_name)
    extension = get_file_extension(file_name)
    file_data = parse(absolute_path, get_format_name(extension))
    return file_data
