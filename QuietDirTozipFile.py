import shutil
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("source_folder", help="Path")
    parser.add_argument("zip_file", help="Path(.zip suffix)")

    args = parser.parse_args()

    source_folder = args.source_folder
    zip_file = args.zip_file

    if os.path.exists(source_folder) and os.path.isdir(source_folder):
        shutil.make_archive(zip_file.replace('.zip', ''), 'zip', source_folder)
        print(f"Finish {source_folder} > {zip_file}")


if __name__ == "__main__":
    main()
