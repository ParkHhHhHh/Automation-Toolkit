import os
import shutil
import argparse


def organize_folder(path):
    """
    Automatically organize files into directories by extension.
    """

    for filename in os.listdir(path):
        src = os.path.join(path, filename)

        if os.path.isfile(src):
            ext = filename.split(".")[-1].lower()
            dest_dir = os.path.join(path, ext)

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.move(src, os.path.join(dest_dir, filename))
            print(f"[MOVE] {filename} → {dest_dir}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Organizer")
    parser.add_argument("--path", required=True, help="Target directory path")
    args = parser.parse_args()

    organize_folder(args.path)
