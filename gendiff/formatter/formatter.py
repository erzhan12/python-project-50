from .stylish import stylish
from .plain import plain
from .json import json_


def format_(result_object, file_format):
    match file_format:
        case 'stylish':
            return stylish(result_object)
        case 'plain':
            return plain(result_object)
        case 'json':
            return json_(result_object)
