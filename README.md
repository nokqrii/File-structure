# Markdown Structure Generator

A lightweight utility that automatically generates a clean Markdown representation of a project's file and folder structure.

Perfect for GitHub repositories, documentation, project overviews, and developer portfolios.

## Features

* Recursive directory scanning
* Clean Markdown output
* Optional `.gitignore` support
* Automatic filtering of common unnecessary folders
* Folder and file statistics
* UTF-8 support
* Works as both a Python script and standalone executable
* Simple interactive interface

## Example Output

```text
.
├── 📁 src/
│   ├── 📄 main.py
│   └── 📄 utils.py
├── 📁 assets/
│   └── 📄 logo.png
├── 📄 README.md
└── 📄 requirements.txt
```

## Installation

### Executable

Download the latest release and run:

```text
MarkdownStructureGenerator.exe
```

### Python

```bash
git clone https://github.com/yourusername/MarkdownStructureGenerator.git
cd MarkdownStructureGenerator
python generate.py
```

## Usage

Launch the program:

```bash
python generate.py
```

or

```bash
MarkdownStructureGenerator.exe
```

The program will ask:

1. Which folder to scan
2. Whether `.gitignore` should be respected

A `structure.md` file will then be generated automatically.

## Roadmap

### v0.2.0-beta

* Custom output filename
* Maximum depth option
* Hidden file support
* Command-line arguments

### Future

* JSON export
* TXT export
* GUI version
* Drag-and-drop support
* Repository analysis statistics

## Version

Current version: **v0.1.0-beta**

## License

MIT License

## Author

Made by Nokqrii
