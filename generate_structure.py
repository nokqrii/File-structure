from pathlib import Path

def generate_markdown_structure(root_dir, indent="", skip_dirs=None):
    """
    Recursively wanders through directories and returns a beautifully 
    formatted visual tree string for Markdown.
    """
    if skip_dirs is None:
        # Ignore common massive dependency/system folders to keep it clean
        skip_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", ".env"}
    
    markdown_str = ""
    root_path = Path(root_dir)
    
    # Separate and sort directories and files for a clean appearance
    try:
        items = sorted(list(root_path.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        return "" # Skip folders you don't have access to read
        
    for index, item in enumerate(items):
        if item.name in skip_dirs or item.name == "structure.md":
            continue
            
        # Determine if this is the last item in the current directory loop
        is_last = (index == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        if item.is_dir():
            markdown_str += f"{indent}{connector}📁 {item.name}/\n"
            # Adjust indentation visual anchors for subfolders
            sub_indent = indent + ("    " if is_last else "│   ")
            markdown_str += generate_markdown_structure(item, sub_indent, skip_dirs)
        else:
            markdown_str += f"{indent}{connector}📄 {item.name}\n"
            
    return markdown_str

if __name__ == "__main__":
    # Scan the current directory where the script is located
    current_directory = Path(".")
    
    print("Scanning directory structure...")
    tree_structure = generate_markdown_structure(current_directory)
    
    # Wrap the output in a clean markdown code block
    markdown_content = f"# Project Structure\n\n```text\n.\n{tree_structure}```\n"
    
    # Write the result directly to structure.md
    output_file = current_directory / "structure.md"
    output_file.write_text(markdown_content, encoding="utf-8")
    
    print(f"Success! Structure written to {output_file.absolute()}")
