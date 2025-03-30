import os
from pathlib import Path

non_table_xml_filename_filters = [
    lambda x: x.endswith(".xml"),
    lambda x: not any((
        x.startswith("TWaD_"),
        x.startswith("TWaDFORMDESCR_"),
        x.startswith("TWaDQUERY"),
        x.startswith("TWADFORMDESCR_"),
    )),
]

if __name__ == '__main__':
    path_assemblykit \
        = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Total War Rome II\assembly_kit")
    db_files = list(filter(
        lambda x: all(_f(x) for _f in non_table_xml_filename_filters),
        os.listdir(path_assemblykit / "raw_data/db")
    ))

    print(f"Length of db_files: {len(db_files)}")

    filename_to_definition_map = {}

    for db_filename in db_files:
        def_filename = "TWaD_" + db_filename
        def_path = path_assemblykit / "raw_data/db" / def_filename
        if not os.path.exists(def_path):
            print(f"File {def_path} does not exist.")
            continue