"""
Each table extracted by RPFM has a version number in header.
Create a file with the latest version of each table.
"""
import json
import os

import sys


def try_open(_fpath):
    """
    Try to open a file and return the content.
    """
    try:
        with open(_fpath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error opening file {_fpath}: {e}")

    return None


if __name__ == '__main__':
    dir_with_tables = r"C:\Users\buk\Downloads\New folder (2)\db"
    file_name = "rpfm_dbtsv_getheader.json"

    tables = {}
    for dirpath, dirnames, filenames in os.walk(dir_with_tables):
        for filename in filenames:
            # get the table name from the directory name
            table_name = os.path.basename(dirpath)
            if table_name not in tables:
                tables[table_name] = []
            # read the first line of the file to get the version number
            content = try_open(os.path.join(dirpath, filename))
            if content is None:
                continue
            data = content[1].strip().split(';')
            tables[table_name].append(
                {'filename': filename.replace('.tsv', ''), 'version': data[1], 'path': data[2], 'table': data[0][1:]})

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(tables, f, indent=4, ensure_ascii=False)
