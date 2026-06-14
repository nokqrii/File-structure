from pathlib import Path
import fnmatch
import sys

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

            if not line or line.startswith("#"):
                continue

            patterns.append(line)

    except Exception:
        pass

    return patterns


def matches_gitignore(path_obj, root_dir, patterns):

    try:
        relative_path = (
            path_obj
            .relative_to(root_dir)
            .as_posix()
        )

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
    gitignore_patterns,
    stats,
    indent=""
):

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

        if item.name in DEFAULT_IGNORES:
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
            index ==
            len(visible_items) - 1
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


def get_root_directory():

    folder = input(
        "\nFolder path "
        "(leave blank for current folder): "
    ).strip()

    if folder:

        root_dir = Path(folder)

        if not root_dir.exists():

            print("\nFolder not found.")
            sys.exit(1)

        return root_dir

    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path.cwd()


def main():

    print("=" * 40)
    print("Markdown Structure Generator")
    print("=" * 40)

    root_dir = get_root_directory()

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

    stats = {
        "folders": 0,
        "files": 0
    }

    print("\nScanning...\n")

    tree = generate_tree(
        root_dir,
        root_dir,
        gitignore_patterns,
        stats
    )

    markdown = f"""# 📂 Project Structure

**Root:** `{root_dir}`

📁 {stats['folders']} folders • 📄 {stats['files']} files

## Directory Tree

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

    print("Done!")
    print(
        f"\nSaved to:\n{output_file}"
    )


if __name__ == "__main__":
    main()
