import pathlib
import os
import json 


def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

def scan_directory(raw_path):

    path = os.path.expandvars(raw_path)
    path = pathlib.Path(path)

    if not path.exists():
        print(f"Path does not exist: {path}")
        return []

    files = []
    for file in path.rglob("*"):
        try:
            if file.is_file():
                files.append(file)
        except OSError as e:
            print(f"Error scanning file {file}: {e}")
            continue

    return files

def format_size(bytes_size):
    size_mb = bytes_size / (1024 * 1024)
    return f"{size_mb:.2f} MB"

def delete_files(files, dry_run=True):
    files_dleted = 0
    files_not_deleted = 0

    for file in files:
        try:
            if dry_run:
                print(f"Dry run: Would delete {file}")
            else:
                file.unlink()
                print(f"Deleted {file}")
                files_dleted += 1
        except OSError as e:
            print(f"Error deleting file {file}: {e}")
            files_not_deleted += 1
    if not dry_run:
        print(f"Files deleted: {files_dleted}, Files not deleted: {files_not_deleted}")

    


def main():


    config = load_config()

    directories = config.get("target_directories", [])
    grand_total_files = 0
    grand_total_bytes = 0
    all_found_files = []

    for path in directories:
        files = scan_directory(path)
        all_found_files.extend(files)

        total_bytes = 0

        for file in files:
            try:
                total_bytes += file.stat().st_size
                
            except OSError:
                continue
        grand_total_files += len(files)
        grand_total_bytes += total_bytes
        print(f"Found {len(files)} files in {path}, we will get rid of {format_size(total_bytes)} of data.")


    if grand_total_files == 0:
        print("No files found to delete.")
        return

    print(f"Grand total: {grand_total_files} files, {format_size(grand_total_bytes)} of data.")
    confirm = input("Czy chcesz usunąć znalezione pliki? (t/n): ").strip().lower()
    if confirm in ["t", "tak", "y", "yes"]:
        delete_files(all_found_files, dry_run=False)
    else:
        print("Operacja anulowana. Żadne pliki nie zostały usunięte.")
   





if __name__ == "__main__":
    main()
