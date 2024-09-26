#!/usr/bin/env python3

import argparse

from gendiff import generate_diff


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    file1, file2, file_format = parse()

    diff = generate_diff(file1, file2, file_format)
    print(diff)


if __name__ == '__main__':
    main()
