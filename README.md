# Py Auto Structure

**Py Auto Structure** is a versatile tool designed to simplify the process of creating directory structures for your Python projects. It leverages YAML files to define project hierarchies and offers a convenient command-line interface for effortless structure creation.

## Features

- **Project Structure Definition:** Define and customize your project structure in a YAML file.
- **Command-Line Interface (CLI):** Create project directories with ease using simple commands.
- **Customization:** Tailor the project name and root folder during structure creation.

## Installation

```bash
pip install py-auto-structure
```

## Usage

### 1. Using it from the command line
Creating a project structure is as easy as running a command in your terminal. Use the following command, replacing **<project_name>** with the desired name:

```bash
py-structure -p <path_to_be_set> -n <project_name>
```

Options:
- -p, --path: Path where the parent directory of the project will be set.
- -n, --name: Specify the name of the project and it will be the root of the project.
- --set-yaml: Path to the YAML file containing the project structure definition. Default is an internal project_structure.yaml.
- --yaml: Returns the raw content of the default yaml in order to copy it.

By default, the script looks for the project structure definition in a file named project_structure.yaml in the current directory.

### 2. Using it as a module

You can also import it as a module and call the function project_build this way:

```python
from project_builder.project_builder import project_build

project_build(path=your_path, yaml_path=your_custom_yaml_path)

```

## Default YAML

Here is as simplified version (in order to improve readability) of the default .yaml used:

```yaml
project_structure:
  - name: data
    type: directory
    content:
      - name: raw
  - name: notebooks
    type: directory
  - name: src
    type: directory
    content:
      - name: __init__.py
        type: file
      - name: feature1
        type: directory
  - name: tests
    type: directory
  - name: docs
    type: directory
  - name: outputs
    type: directory
  - name: requirements.txt
    type: file
  - name: main.py
    type: file
    content: 
      >
        def main():
            print("Hello World!")

        if __name__ == "__main__":
            main()
```

You can customize the default passing your own .yaml path to the function but this would create the following structure:

```lua
MyProject/
|-- data/
|   `-- raw/
|-- notebooks/
|-- src/
|   |-- __init__.py
|   `-- feature1/
|-- tests/
|-- docs/
|-- outputs/
|-- requirements.txt
|-- main.py
```

Make sure to follow this structure for the custom yaml:

```yaml
name: <dirname | filename>
type: <file | directory>
content: <list for directories | string for files>
```