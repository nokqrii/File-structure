````python
from pathlib import Path
import fnmatch
import sys

# Default directories to ignore
DEFAULT_IGNORES = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".env",
    "node_modules",
    ".idea",
    ".vscode",
    "dist",
    "build"
}


def load_gitignore(root_dir):
    """
    Load patterns from .gitignore
    """
    gitignore_file = root_dir / ".gitignore"

    if not gitignore_file.exists():
        return []

    patterns = []

    try:
        for line in gitignore_file.read_text(
            encoding="utf-8",
            errors="ignore"
        ).splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            patterns.append(line)

    except Exception:
        pass

    return patterns


def matches_gitignore(path_obj, root_dir, patterns):
    """
    Check whether a path matches .gitignore rules
    """
    try:
        relative_path = path_obj.relative_to(root_dir).as_posix()
    except ValueError:
        return False

    for pattern in patterns:

        pattern = pattern.rstrip("/")

        if fnmatch.fnmatch(relative_path, pattern):
            return True

        if fnmatch.fnmatch(path_obj.name, pattern):
            return True

        if relative_path.startswith(pattern + "/"):
            return True

    return False


def generate_tree(
    root_dir,
    current_dir,
    gitignore_patterns=None,
    skip_dirs=None,
    stats=None,
    indent=""
):
    """
    Generate Markdown tree recursively
    """

    if skip_dirs is None:
        skip_dirs = set()

    if gitignore_patterns is None:
        gitignore_patterns = []

    if stats is None:
        stats = {
            "files": 0,
            "folders": 0
        }

    try:
        items = sorted(
            current_dir.iterdir(),
            key=lambda x: (
                not x.is_dir(),
                x.name.lower()
            )
        )

    except PermissionError:
        return ""

    visible_items = []

    for item in items:

        if item.name in skip_dirs:
            continue

        if item.name == "structure.md":
            continue

        if matches_gitignore(
            item,
            root_dir,
            gitignore_patterns
        ):
            continue

        visible_items.append(item)

    tree = ""

    for index, item in enumerate(visible_items):

        is_last = (
            index == len(visible_items) - 1
        )

        connector = (
            "└── "
            if is_last
            else "├── "
        )

        if item.is_dir():

            stats["folders"] += 1

            tree += (
                f"{indent}"
                f"{connector}"
                f"📁 {item.name}/\n"
            )

            next_indent = (
                indent +
                (
                    "    "
                    if is_last
                    else "│   "
                )
            )

            tree += generate_tree(
                root_dir,
                item,
                gitignore_patterns,
                skip_dirs,
                stats,
                next_indent
            )

        else:

            stats["files"] += 1

            tree += (
                f"{indent}"
                f"{connector}"
                f"📄 {item.name}\n"
            )

    return tree


def main():

    print("=" * 50)
    print("Markdown Project Structure Generator")
    print("=" * 50)

    target = input(
        "\nFolder path "
        "(leave blank for current folder): "
    ).strip()

    if target:

        root_dir = Path(target)

        if not root_dir.exists():

            print("\n[ERROR] Folder not found.")
            return

    else:

        if getattr(sys, "frozen", False):

            root_dir = (
                Path(sys.executable)
                .parent
            )

        else:

            root_dir = (
                Path.cwd()
            )

    use_gitignore = (
        input(
            "\nRespect .gitignore? (Y/N): "
        )
        .strip()
        .lower()
        == "y"
    )

    gitignore_patterns = []

    if use_gitignore:

        gitignore_patterns = (
            load_gitignore(root_dir)
        )

        print(
            f"\nLoaded "
            f"{len(gitignore_patterns)} "
            f".gitignore patterns."
        )

    stats = {
        "files": 0,
        "folders": 0
    }

    print("\nScanning...\n")

    tree = generate_tree(
        root_dir=root_dir,
        current_dir=root_dir,
        gitignore_patterns=gitignore_patterns,
        skip_dirs=DEFAULT_IGNORES,
        stats=stats
    )

    markdown = f"""# Project Structure

Generated from:

`{root_dir}`

## Statistics

- Folders: {stats['folders']}
- Files: {stats['files']}

```text
.
{tree}```
"""

    output_file = (
        root_dir /
        "structure.md"
    )

    output_file.write_text(
        markdown,
        encoding="utf-8"
    )

    print(
        f"Done!\n\n"
        f"Folders: {stats['folders']}\n"
        f"Files: {stats['files']}\n\n"
        f"Saved to:\n"
        f"{output_file.absolute()}"
    )


if __name__ == "__main__":
    main()
````
