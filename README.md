<img width="1919" height="1003" alt="image" src="https://github.com/user-attachments/assets/6067221d-b37a-459f-b979-d445860ccd71" />
# Markdown Structure Generator

Generate clean Markdown representations of directory and repository structures directly from the command line.

## Overview

Markdown Structure Generator is a lightweight utility designed for developers who want to quickly document project structures for GitHub repositories, documentation, portfolio projects, bug reports, and discussions.

The tool recursively scans a directory and generates a visual tree structure in Markdown format.

## Features

* Recursive directory scanning
* Clean Markdown tree generation
* Automatic `structure.md` creation
* Optional `.gitignore` support
* File and folder statistics
* Automatic filtering of common development folders
* UTF-8 support
* Standalone Windows executable
* No dependencies required when using the executable

## Example

Input:

```text id="24q4ic"
MyProject/
├── src/
├── docs/
├── README.md
└── requirements.txt
```

Generated output:

```text id="gng6rz"
# Project Structure

## Statistics

- Folders: 2
- Files: 2

.
├── 📁 src/
├── 📁 docs/
├── 📄 README.md
└── 📄 requirements.txt
```

## Installation

### Download Executable

Download the latest release from the Releases section and run:

```text id="y4lzlg"
MarkdownStructureGenerator.exe
```

### Run From Source

```bash id="o3mjlwm"
git clone https://github.com/nokqrii/MarkdownStructureGenerator.git
cd MarkdownStructureGenerator
python generate.py
```

## Usage

Launch the program:

```bash id="l7n7m5"
python generate.py
```

or

```bash id="hclu2q"
MarkdownStructureGenerator.exe
```

The program will:

1. Ask for a target folder
2. Ask whether `.gitignore` should be respected
3. Scan the directory
4. Generate a `structure.md` file

## Ignored Directories

By default, common development directories are excluded:

```text id="gaj7ki"
.git
__pycache__
.venv
venv
.env
node_modules
.idea
.vscode
dist
build
```

## Planned Features

* Custom output filename
* Maximum scan depth
* JSON export
* TXT export
* Command-line arguments
* Clipboard support

## License

MIT License

## Author

Nokqrii

## Contributing

Issues, suggestions, and pull requests are welcome.
