from gendiff.scripts.file_reader import read_file
from gendiff.formatter.formatter import format_


def gen_diff_object(obj1, obj2):
    """
    Generate a diff between two dictionaries.
    """

    def is_dict(value):
        return isinstance(value, dict)

    def assign_value(value):
        if is_dict(value):
            return gen_diff_object(value, value)
        return value

    keys = sorted(obj1.keys() | obj2.keys())
    result = list()

    for key in keys:
        val1 = obj1.get(key)
        val2 = obj2.get(key)

        if key in obj1 and key in obj2:
            if is_dict(val1) and is_dict(val2):
                result.append({
                    'key': key,
                    'type': 'objects',
                    'value': gen_diff_object(val1, val2),
                })
            elif val1 == val2:
                result.append({
                    'key': key,
                    'type': 'equal',
                    'value': assign_value(val1),
                })
            else:
                result.append({
                    'key': key,
                    'type': 'changed',
                    'oldValue': assign_value(val1),
                    'newValue': assign_value(val2),
                })
        elif key in obj1:
            result.append({
                'key': key,
                'type': 'removed',
                'oldValue': assign_value(val1),
            })
        else:
            result.append({
                'key': key,
                'type': 'added',
                'newValue': assign_value(val2),
            })
    return result


def generate_diff(file1, file2, file_format='stylish'):
    data1 = read_file(file1)
    data2 = read_file(file2)

    result_object = gen_diff_object(data1, data2)
    result_string = format_(result_object, file_format)

    return result_string
