def stylish(tree, indent='  '):
    """
    Formats the diff tree into a stylish string representation.
    """

    def to_string(value):
        if isinstance(value, bool):  # true or false
            return str(value).lower()
        elif value is None:          # null
            return 'null'
        else:
            return str(value)

    def iter_(element, depth=1):
        if isinstance(element, list):
            value_indent = indent * (2 * depth - 1)
            bracket_indent = indent * (2 * depth - 2)
            lines = []

            for node in element:
                key = node['key']
                node_type = node['type']

                if node_type == 'removed':
                    lines.append(f"{value_indent}- {key}: "
                                 f"{iter_(node['oldValue'], depth + 1)}")
                elif node_type == 'added':
                    lines.append(f"{value_indent}+ {key}: "
                                 f"{iter_(node['newValue'], depth + 1)}")
                elif node_type == 'changed':
                    lines.extend([
                        f"{value_indent}- {key}: "
                        f"{iter_(node['oldValue'], depth + 1)}",
                        f"{value_indent}+ {key}: "
                        f"{iter_(node['newValue'], depth + 1)}"
                    ])
                elif node_type in ('equal', 'objects'):
                    lines.append(f"{value_indent}  {key}: "
                                 f"{iter_(node['value'], depth + 1)}")
                else:
                    pass

            return '\n'.join(['{', *lines, f'{bracket_indent}}}'])

        elif isinstance(element, dict):
            value_indent = indent * (2 * depth)
            bracket_indent = indent * (2 * depth - 2)
            lines = []

            for key, value in element.items():
                lines.append(f"{value_indent}{key}: {iter_(value, depth + 1)}")

            return '\n'.join(['{', *lines, f"{bracket_indent}}}"])

        else:
            return to_string(element)

    return iter_(tree)
