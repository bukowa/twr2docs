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
    dir_with_tables = r"C:\Users\buk\Downloads\r2\assembly\db"
    file_name = "rpfm_dbtsv_getheader_assembly.json"

    tables = {}
    for dirpath, dirnames, filenames in os.walk(dir_with_tables):

        table_name = os.path.basename(dirpath)
        if table_name not in tables:
            tables[table_name] = []

        for filename in filenames:
            # get the table name from the directory name
            # read the first line of the file to get the version number
            content = try_open(os.path.join(dirpath, filename))
            if content is None:
                continue
            data = content[1].strip().split(';')

            # if filename ends with _tables, trim it (assemblykit)
            if filename.endswith("_tables.tsv"):
                filename = filename[:-len("_tables.tsv")]

            # if path ends with _tables, trim it (assemblykit)
            if data[2].endswith("_tables"):
                data[2] = data[2][:-len("_tables")]

            tables[table_name].append(
                {'filename': filename.replace('.tsv', ''), 'version': data[1], 'path': data[2], 'table': data[0][1:]})



        # if list is empty, remove
        # if not tables[table_name]:
        #     del tables[table_name]

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(tables, f, indent=4, ensure_ascii=False)
