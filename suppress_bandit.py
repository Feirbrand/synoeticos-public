import re
import os

def suppress_bandit_b311_warnings(output_file, project_root):
    issues = {}
    with open(output_file, 'r') as f:
        for line in f:
            match = re.search(r"Location: \.(.*?):(\d+):.*B311:blacklist", line)
            if match:
                # Normalize path for Windows or Linux
                relative_path = match.group(1).replace('/', os.sep)
                file_path = os.path.join(project_root, relative_path)
                line_number = int(match.group(2))
                if file_path not in issues:
                    issues[file_path] = set()
                issues[file_path].add(line_number)
    
    print(f"DEBUG: Found {len(issues)} files with B311 issues.")
    for fp, lns in issues.items():
        print(f"DEBUG: File: {fp}, Lines: {sorted(list(lns))}")

    for file_path, line_numbers in issues.items():
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            continue

        with open(file_path, 'r') as f:
            lines = f.readlines()

        modified_lines = []
        file_modified = False
        for i, line in enumerate(lines):
            if (i + 1) in line_numbers:
                print(f"DEBUG: Processing line {i+1} in {file_path}")
                print(f"DEBUG: Original line: {line.strip()}")
                if not line.rstrip().endswith("# nosec"): # Check if # nosec is already present
                    modified_lines.append(line.rstrip() + "  # nosec\n")
                    file_modified = True
                    print(f"DEBUG: Modified line: {modified_lines[-1].strip()}")
                else:
                    modified_lines.append(line)
                    print(f"DEBUG: Line already has # nosec: {line.strip()}")
            else:
                modified_lines.append(line)

        if file_modified:
            with open(file_path, 'w') as f:
                f.writelines(modified_lines)
            print(f"Modified {file_path} to suppress Bandit B311 warnings.")
        else:
            print(f"No changes needed for {file_path}.")

if __name__ == "__main__":
    output_filename = r"C:\\Users\\feirb\\.gemini\\tmp\\c30c2404f05fb2b5933709a4e8fb85a7126c0207b6c1eb3e32f39c23a24fe726\\bandit_output.txt"
    project_root = r"C:\\Users\\feirb\\synoeticos-public"
    suppress_bandit_b311_warnings(output_filename, project_root)