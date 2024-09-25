def next_property(current_property, new_key):
    result = new_key \
        if current_property == '' \
        else f"{current_property}.{new_key}"
    return result


def to_string(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (dict, list)):
        return '[complex value]'
    return str(value)


def plain(tree):
    def iter_(element, property_=''):
        if not isinstance(element, list):
            return to_string(element)

        lines = []
        for node in element:
            node_type = node.get('type')
            node_key = node.get('key')
            next_prop = next_property(property_, node_key)

            if node_type == 'removed':
                lines.append(f"Property '{next_prop}' was removed")

            elif node_type == 'added':
                new_value = node.get('newValue')
                value_str = to_string(new_value)
                lines.append(
                    f"Property '{next_prop}' was added with value: {value_str}"
                )

            elif node_type == 'changed':
                old_value = node.get('oldValue')
                new_value = node.get('newValue')
                old_value_str = to_string(old_value)
                new_value_str = to_string(new_value)
                lines.append(
                    f"Property '{next_prop}' was updated. "
                    f"From {old_value_str} to {new_value_str}"
                )

            elif node_type == 'objects':
                lines.extend(iter_(node.get('value'), next_prop))

        return lines

    return '\n'.join(iter_(tree))
