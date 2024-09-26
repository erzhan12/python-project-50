from gendiff.generate_diff import generate_diff


def test_stylish_json():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    actual = generate_diff(file1, file2)
    expected = open('gendiff/tests/fixtures/expected_stylish.txt', 'r').read()
    assert actual == expected


def test_stylish_yaml():
    file1 = 'gendiff/tests/fixtures/file1.yml'
    file2 = 'gendiff/tests/fixtures/file2.yml'
    actual = generate_diff(file1, file2)
    expected = open('gendiff/tests/fixtures/expected_stylish.txt', 'r').read()
    assert actual == expected


def test_plain_json():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    actual = generate_diff(file1, file2, 'plain')
    expected = open('gendiff/tests/fixtures/expected_plain.txt', 'r').read()
    assert actual == expected


def test_json_json():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    actual = generate_diff(file1, file2, 'json')
    expected = open('gendiff/tests/fixtures/expected_json.txt', 'r').read()
    assert actual == expected
