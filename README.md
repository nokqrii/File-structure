# Markdown Structure Generator

A lightweight utility that generates a clean Markdown representation of a project's file and folder structure.

Perfect for:

* GitHub repositories
* Documentation
* Project overviews
* Portfolio projects
* Sharing repository structures

## Features

* Generates a visual tree structure
* Outputs directly to `structure.md`
* Supports `.gitignore` filtering
* Ignores common unnecessary folders
* Works as both a Python script and a standalone executable
* UTF-8 support
* Recursive directory scanning
* Folder and file statistics

## Example Output

```text
.
├── 📁 src/
│   ├── 📄 main.py
│   └── 📄 utils.py
├── 📁 docs/
│   └── 📄 guide.md
├── 📄 README.md
└── 📄 requirements.txt
```

## Installation

### Option 1: Download Release

Download the latest executable from the Releases page and run it.

### Option 2: Run from Source

```bash
git clone <repository-url>
cd markdown-structure-generator
python generate_structure.py
```

## Usage

Run the program:

```bash
python generate_structure.py
```

or

```bash
generate_structure.exe
```

The program will ask:

* Which folder to scan
* Whether `.gitignore` rules should be respected

After scanning, a `structure.md` file will be generated.

## Roadmap

Planned features:

* Custom output filename
* Maximum depth option
* JSON export
* Plain text export
* Hidden file support
* Command-line arguments
* Faster scanning for large repositories

## Version

Current Release: v0.1.0-beta

## License

MIT License

## Author

Created by Abhijit A. Mishra
