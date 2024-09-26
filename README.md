### Hexlet tests and linter status:
[![Actions Status](https://github.com/erzhan12/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/erzhan12/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/1e4a9529e817bd5e52e0/maintainability)](https://codeclimate.com/github/erzhan12/python-project-50/maintainability)

[![Maintainability](https://api.codeclimate.com/v1/badges/1e4a9529e817bd5e52e0/maintainability)](https://codeclimate.com/github/erzhan12/python-project-50/maintainability)
---
### Description:
The package functionality is finding differences between two given files (.json or .yaml)
Following formats are supported:

- stylish - structured view
- plain - plain view
- json - output in json format

Command line execution:
> gendiff --format stylish file_path1.json file_path2.json

Usage in your own code:
```
diff = generate_diff(file_path1, file_path2, format_name)
```

### Demo:
[![asciicast](https://asciinema.org/a/is8pgGnwsqix5SMeT8lIM7Udb.svg)](https://asciinema.org/a/is8pgGnwsqix5SMeT8lIM7Udb)
